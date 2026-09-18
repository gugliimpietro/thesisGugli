# Membaca struktur indus07.accdb (atau .accdb lain) dan mengekspor SEMUA tabelnya ke CSV.
#
# CARA PAKAI (PowerShell, bukan Excel):
#   1. Buka PowerShell biasa (tidak perlu Admin) di folder scripts:
#        cd "D:\kuliah s2\1. tesis\thesisGugli\scripts"
#   2. Jalankan:
#        .\export_indus_accdb.ps1
#      (secara default mencari file di bawah ini; ganti $mdb jika lokasinya beda)
#
# Kenapa PowerShell, bukan Excel: teknik ini sudah pernah berhasil membaca
# ImporIndonesia.mdb (menghasilkan data\mdb_struktur.txt), jadi driver Access
# di komputer Anda sudah terbukti jalan. Excel "Get Data from Access" memakai
# driver yang sama, tapi sering gagal kalau Office 32-bit sedangkan drivernya
# 64-bit (atau sebaliknya) -- PowerShell ini menghindari masalah itu, dan
# tidak dibatasi baris/kolom seperti membuka file besar di lembar kerja Excel.
#
# HASIL:
#   data\indus_struktur.txt         daftar tabel, kolom, jumlah baris
#   data\<NamaTabel>.csv             satu CSV per tabel (tabel sistem dilewati)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$mdb  = Join-Path $root "..\bahan tesis\data\data IBS 1990-2013\Data industri manufaktur\Industri Manufaktur_2005-2011\Akses\indus07.accdb"
$mdb  = [System.IO.Path]::GetFullPath($mdb)
$outStruct = Join-Path $root "data\indus_struktur.txt"
$outDir    = Join-Path $root "data"

if (-not (Test-Path $mdb)) {
    Write-Host "TIDAK DITEMUKAN: $mdb"
    Write-Host "Edit baris `$mdb di bagian atas skrip ini dan tunjuk ke lokasi indus07.accdb yang benar."
    exit 1
}

$providers = @("Microsoft.ACE.OLEDB.12.0","Microsoft.ACE.OLEDB.16.0","Microsoft.Jet.OLEDB.4.0")
$conn = New-Object -ComObject ADODB.Connection
$opened = $false
foreach ($p in $providers) {
    try { $conn.Open("Provider=$p;Data Source=$mdb;"); $opened = $true; Write-Host "Terhubung dengan $p"; break }
    catch { Write-Host "Gagal dengan $p" }
}
if (-not $opened) {
    Write-Host ""
    Write-Host "Tidak ada provider yang bisa membuka file."
    Write-Host "Pasang 'Microsoft Access Database Engine 2016 Redistributable' (pilih versi 64-bit"
    Write-Host "kalau Office Anda 64-bit): https://www.microsoft.com/en-us/download/details.aspx?id=54920"
    exit 1
}

$lines = @("STRUKTUR $([System.IO.Path]::GetFileName($mdb))", "Dibaca: $(Get-Date -Format 'yyyy-MM-dd HH:mm')", "")

# adSchemaTables = 20
$rs = $conn.OpenSchema(20)
$tables = @()
while (-not $rs.EOF) {
    $type = $rs.Fields.Item("TABLE_TYPE").Value
    $name = $rs.Fields.Item("TABLE_NAME").Value
    if ($type -eq "TABLE" -and $name -notlike "MSys*" -and $name -notlike "~*") {
        $tables += $name
    }
    $rs.MoveNext()
}
$rs.Close()

$lines += "Jumlah tabel data: $($tables.Count)"
$lines += ""

foreach ($t in $tables) {
    try {
        $c = $conn.Execute("SELECT COUNT(*) AS n FROM [$t]")
        $n = $c.Fields.Item("n").Value
        $c.Close()
    } catch { $n = "?" }

    $lines += "=== $t  ($n baris) ==="

    try {
        $rec = $conn.Execute("SELECT * FROM [$t]")
        $cols = @()
        for ($i = 0; $i -lt $rec.Fields.Count; $i++) { $cols += $rec.Fields.Item($i).Name }
        $lines += "kolom (" + $cols.Count + "): " + ($cols -join " | ")

        $csvPath = Join-Path $outDir ("$t.csv")
        $sw = New-Object System.IO.StreamWriter($csvPath, $false, [System.Text.Encoding]::UTF8)
        $sw.WriteLine(($cols -join ","))
        $rowCount = 0
        while (-not $rec.EOF) {
            $vals = @()
            for ($i = 0; $i -lt $rec.Fields.Count; $i++) {
                $v = $rec.Fields.Item($i).Value
                if ($null -eq $v) { $v = "" }
                $v = "$v" -replace '"','""'
                if ($v -match '[,"\r\n]') { $v = '"' + $v + '"' }
                $vals += $v
            }
            $sw.WriteLine(($vals -join ","))
            $rowCount++
            $rec.MoveNext()
        }
        $sw.Close()
        $rec.Close()
        $lines += "  -> diekspor ke data\$t.csv ($rowCount baris)"
        Write-Host "  $t -> $rowCount baris ditulis ke $csvPath"
    } catch {
        $lines += "  (gagal mengekspor: $_)"
        Write-Host "  GAGAL mengekspor $t : $_"
    }
    $lines += ""
}

$conn.Close()
$lines | Out-File -FilePath $outStruct -Encoding UTF8

Write-Host ""
Write-Host "Selesai. Struktur ditulis ke: $outStruct"
Write-Host "Semua tabel data sudah diekspor sebagai CSV di folder data\"
Write-Host "Commit & push, lalu beri tahu Claude nama tabel utamanya (biasanya yang baris-nya paling banyak)."
