Summary:	Transparent editing of GPG public/private-key encrypted files
Summary(pl.UTF-8):	Przezroczysta edycja plików szyfrowaych kluczami publicznymi/prywatnymi GPG
Name:		vim-plugin-gnupg
Version:	1.27
Release:	1
License:	GPL
Group:		Applications/Editors/Vim
Source0:	gnupg.vim
# Source0-md5:	b7d56cdb65183bb12fac04316a244297
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=661
# for _vimdatadir existence
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This script implements transparent editing of GPG public/private-key
encrypted files. The filename must have a ".gpg" suffix. When opening
such a file the content is decrypted, when opening a new file the
script will ask for the recipients of the encrypted file. The file
content will be encrypted to all recipients before it is written. The
script turns off viminfo and swapfile to increase security.

%description -l pl.UTF-8
Ten skrypt implementuje przezroczystą edycję plików szyfrowanych
kluczami publicznymi/prywatnymi GPG. Nazwa pliku musi mieć przyrostek
".gpg". Przy otwieraniu takiego pliku zawartość jest odszyfrowywana,
natomiast przy tworzeniu nowego pliku skrypt pyta o adresatów
zaszyfrowanego pliku. Przed zapisem zawartość pliku zostaje
zaszyfrowana dla wszystkich adresatów. Aby zwiększyć bezpieczeństwo
skrypt wyłącza viminfo i swapfile.

%prep

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_vimdatadir}/plugin
cp -a %{SOURCE0} $RPM_BUILD_ROOT%{_vimdatadir}/plugin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_vimdatadir}/plugin/*
