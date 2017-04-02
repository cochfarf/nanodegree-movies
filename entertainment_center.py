import fresh_tomatoes
import media

#defining each movie instances
toy_story = media.Movie("Toy Story",
 "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")
avatar = media.Movie("Avatar",
 "A marine on an alien planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=5PSNL1qE6VY")

big_trouble = media.Movie("Big Trouble in Little China",
 "Truck driver runs into the supernatural in Little China",
 "https://images-na.ssl-images-amazon.com/images/I/51%2BxN8wM76L._AC_UL320_SR210,320_.jpg", "https://www.youtube.com/watch?v=592EiTD2Hgo")

school_of_rock = media.Movie("School of Rock","Using rock music to learn","http://img.moviepostershop.com/the-school-of-rock-movie-poster-2003-1020191888.jpg","https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille","A rat is a chef in Paris","http://www.pixartalk.com/wp-content/uploads/2009/06/ratus1.jpg","https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
 "Going back in time to meet authors","https://images-na.ssl-images-amazon.com/images/I/61uuYEUFw4L._SY450_.jpg","https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
 "Lame tween post apocalyptic story","https://images-na.ssl-images-amazon.com/images/I/51OGv-AnD6L.jpg","https://www.youtube.com/watch?v=LrXIG4oK7Ew")

#list of movie instances
movies = [toy_story, avatar, big_trouble, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

#call fresh_tomatoes.py which creates the web page
fresh_tomatoes.open_movies_page(movies)
