import media
import fresh_tomatoes

# Creates the instances of the Movie

wall_e = media.Movie("Wall_E ",
                     "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",   # NOQA
                     "https://www.youtube.com/watch?v=alIq_wG9FNk")

ice_age = media.Movie("Ice Age",
                      "https://upload.wikimedia.org/wikipedia/en/3/3c/Ice_Age_%282002_film%29_poster.jpg",   # NOQA
                      "https://www.youtube.com/watch?v=5utbt2Ycenw")

frozen = media.Movie("Frozen",
                     "https://upload.wikimedia.org/wikipedia/en/0/05/Frozen_%282013_film%29_poster.jpg",   # NOQA
                     "https://www.youtube.com/watch?v=TbQm5doF_Uc")

cinderella = media.Movie("Cinderella",
                         "https://upload.wikimedia.org/wikipedia/en/c/c2/Cinderella_2015_official_poster.jpg",   # NOQA
                         "https://www.youtube.com/watch?v=20DF6U1HcGQ")

minions = media.Movie("Minions",
                      "https://upload.wikimedia.org/wikipedia/en/3/3d/Minions_poster.jpg",   # NOQA
                      "https://www.youtube.com/watch?v=LYUJPcgBUeE")

inside_out = media.Movie("Inside Out",
                         "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",   # NOQA
                         "https://www.youtube.com/watch?v=YEk_5aT5Gng")
# Making a list of movies

movies = [wall_e, ice_age, frozen, cinderella, minions, inside_out]  # list that stores all the favorite movies

fresh_tomatoes.open_movies_page(movies)

