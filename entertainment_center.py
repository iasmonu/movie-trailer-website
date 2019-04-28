import fresh_tomatoes
import media
# instance with name toystory
toy_story = media.Movie("toy story",
                        "a story of boy and his toys coming to life",
                        "https://upload.wikimedia.org/wikipedia/en/" +
                        "1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=rNk1Wi8SvNc")
# instance of class Movie named avatar
avatar = media.Movie("avatar",
                     "a marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/sco" +
                     "/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
# instance of class Movie named avengers
avengers = media.Movie("avengers infinity war",
                       "a team of super heroes saving earth from thanos",
                       "https://upload.wikimedia.org/wikipedia/en/4/4d/" +
                       "Avengers_Infinity_War_poster.jpg",
                       "https://www.youtube.com/watch?v=6ZfuNTqbHE8")
# instance of class Movie named gullyboy
gullyboy = media.Movie("Gully boy",
                       "a story of a boy who challenges society " +
                       "to achieve big with his rap",
                       "https://upload.wikimedia.org/wikipedia/" +
                       "en/0/07/Gully_Boy_poster.jpg",
                       "https://www.youtube.com/watch?v=JfbxcD6biOk")
# instance of class Movie named gullyboy
shazam = media.Movie("Shazam",
                     "a teenage boy gets superpower and tries to save" +
                     "the world against the evil",
                     "https://upload.wikimedia.org/wikipedia/en/6/60/" +
                     "Shazam%21_theatrical_poster.jpg",
                     "https://www.youtube.com/watch?v=go6GEIrcvFY")
# instance of class Movie named dhoni
dhoni = media.Movie("Ms dhoni - the untold story",
                    "a small town boy fights his way through to " +
                    "become captain of indian team",
                    "https://upload.wikimedia.org/wikipedia/en/3/33/" +
                    "M.S._Dhoni_-_The_Untold_Story_poster.jpg",
                    "https://www.youtube.com/watch?v=6L6XqWoS8tw")
# instance of class Movie named warcraft
warcraft = media.Movie("warcraft",
                       "portrays the initial encounters between the humans" +
                       "and the orcs",
                       "https://upload.wikimedia.org/wikipedia/" +
                       "en/5/56/Warcraft_Teaser_Poster.jpg",
                       "https://www.youtube.com/watch?v=2Rxoz13Bthc")
movies = [toy_story, avengers, gullyboy, shazam, dhoni, warcraft]
fresh_tomatoes.open_movies_page(movies)
# calling the fresh_tomato.py for the webpage outline
