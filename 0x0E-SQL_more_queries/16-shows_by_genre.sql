-- list genre name by show
SELECT tv_shows.title, tv_genres.name
FROM tv_show_genres
JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
RIGHT JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
ORDER BY title, name;
