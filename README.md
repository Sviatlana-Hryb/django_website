Strona została napisana przy użyciu Bootstrap. Struktura serwisu napisana jest własnym stylem, strona przystosowana jest również do urządzeń mobilnych. Witryna zawiera „stronę z podziękowaniem”, która potwierdza wysłanie zgłoszenia i kopiuje nazwę użytkownika. Edycję serwisu można przeprowadzić poprzez panel administracyjny (praca z żądaniami: dodawanie statusu lub komentarza; slajdy karuzeli, dodawanie lub zmiana zdjęć; zmiana cen i usług; ustawienia bota telegramu)

Architektura projektu witryny:

tytuł;
suwak (obraz, tytuł i tekst);
blok „Pakiety serwisowe”: tekst ze statystyk i ceny można edytować z panelu administratora;
tabela „ceny usług” (nazwa usługi, stara cena i nowa),
formularz zgłoszeniowy, po wysłaniu którego zostanie utworzony rekord w bazie danych i na czacie zostanie wysłana wiadomość o nowym zgłoszeniu (nazwa i numer)
Informacje kontaktowe
Aplikacje w panelu administracyjnym: CRM (wniosek, status, komentarz); CMS (slider z karuzelą, zmiana zdjęć i tekstu) CENA (informacje o cenach i usługach) TELEBOT (ustawienia wysyłania wiadomości o wypełnionej aplikacji do czatu)
