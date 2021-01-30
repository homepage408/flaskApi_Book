
SELECT user.id_user, user.nama, level.keterangan
FROM user
INNER JOIN level 
ON user.level = level.id_level;
SELECT * FROM flask_api_book.user;

SELECT user.npm, user.id_user, user.nama, level.keterangan, mahasiswa.npm, prodi.nama_prodi, fakultas.nama_fakultas
FROM user
INNER JOIN mahasiswa
INNER JOIN prodi
INNER JOIN fakultas
INNER JOIN level 
ON user.level = level.id_level and user.npm = mahasiswa.npm and mahasiswa.prodi = prodi.id_prodi and prodi.id_fakultas = fakultas.id_fakultas;

use flask_api_book;

select * from mahasiswa;

select mahasiswa.npm, mahasiswa.nama, mahasiswa.no_hp, mahasiswa.angkatan, mahasiswa.alamat, prodi.nama_prodi, fakultas.nama_fakultas
from mahasiswa
inner join prodi
inner join fakultas
on mahasiswa.prodi = prodi.id_prodi and prodi.id_fakultas = fakultas.id_fakultas
where mahasiswa.npm = 5160411059;





