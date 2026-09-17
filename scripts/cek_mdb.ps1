# Membaca struktur ImporIndonesia.mdb dan mengekspor tabel ke CSV.
# Jalankan di PowerShell:  .\scripts\cek_mdb.ps1
# Hasil: data\mdb_struktur.txt  (daftar tabel, kolom, jumlah baris)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$mdb  = Join-Path $root "data\ImporIndonesia.mdb"
$out  = Join-Path $root "data\mdb_struktur.txt"

if (-not (Test-Path $mdb)) { Write-Host "TIDAK DITEMUKAN: $mdb"; exit 1 }

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
    Write-Host "Pasang 'Microsoft Access Database Engine 2016 Redistributable' versi 64-bit,"
    Write-Host "atau buka file ini langsung di Microsoft Access."
    exit 1
}

$lines = @("STRUKTUR ImporIndonesia.mdb", "Dibaca: $(Get-Date -Format 'yyyy-MM-dd HH:mm')", "")

# adSchemaTables = 20
$rs = $conn.OpenSchema(20)
$tables = @()
while (-not $rs.EOF) {
    if ($rs.Fields.Item("TABLE_TYPE").Value -eq "TABLE") {
        $tables += $rs.Fields.Item("TABLE_NAME").Value
    }
    $rs.MoveNext()
}
$rs.Close()

$lines += "Jumlah tabel: $($tables.Count)"
$lines += ""

foreach ($t in $tables) {
    try {
        $c = $conn.Execute("SELECT COUNT(*) AS n FROM [$t]")
        $n = $c.Fields.Item("n").Value
        $c.Close()
    } catch { $n = "?" }

    $lines += "=== $t  ($n baris) ==="
    try {
        $r = $conn.Execute("SELECT TOP 1 * FROM [$t]")
        $cols = @()
        for ($i = 0; $i -lt $r.Fields.Count; $i++) {
            $f = $r.Fields.Item($i)
            $cols += "$($f.Name)"
        }
        $lines += "kolom: " + ($cols -join " | ")
        if (-not $r.EOF) {
            $vals = @()
            for ($i = 0; $i -lt $r.Fields.Count; $i++) { $vals += "$($r.Fields.Item($i).Value)" }
            $lines += "contoh: " + ($vals -join " | ")
        }
        $r.Close()
    } catch { $lines += "  (gagal membaca kolom: $_)" }
    $lines += ""
}

$conn.Close()
$lines | Out-File -FilePath $out -Encoding UTF8
Write-Host ""
Write-Host "Selesai. Hasil ditulis ke: $out"
Write-Host "Kirimkan isi berkas itu ke Claude untuk langkah berikutnya."
