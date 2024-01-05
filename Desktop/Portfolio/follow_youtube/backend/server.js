import express from "express"
const app = express();
app.use(express.json())
app.use(express.urlencoded({extended : false}))

import cors from 'cors';
app.use(cors({
    origin: 'http://localhost:3000',
    methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
    credentials: true,
}));

/*=================================
        Database
===================================*/
import mongoose from 'mongoose';

mongoose.connect("mongodb+srv://davidfranco923:Ventoaureo@animewebsite.x6da3dw.mongodb.net/",{
    useNewUrlParser: true,
    useUnifiedTopology : true,
}).then(()=>{
    console.log("Connection Successfull")
}).catch((err)=>{
    console.error("MongoDB Connection Error:", err)
})
/************schema*********** */
const userSchema = new mongoose.Schema({
    firstName : String,
    lastName : String,
    email : {
        type: String,
        required :true,
        unique : true,
    },
    password : String
})
const UserModel = new mongoose.model("UserModel",userSchema)

const animeSchema = new mongoose.Schema({
    title: {
        type: String, 
        required: true
    },
    genres: [
        { genre: {
            type: String
        }}
    ],
    episodes: {
        type: Number, 
        required: true
    },
    currentEpisode: {
        type: Number, 
        default: 0
    },
    description: {
        type: String
    },
    image: {
        type: String
    },
    characters: [
        {name: {
            type: String
        }}
    ],
    status: {
        type: String, 
        enum: ['Planning', 'Watching', 'Completed'], 
        default: 'Planning'}
});

const AnimeModel = mongoose.model('AnimeModel', animeSchema);

/*=================================
            put
===================================*/
app.put('/browse/:id/status', async (req, res) => {
    try {
        const animeId = req.params.id;
        const { currentEpisode, status } = req.body;
        console.log(status);

        // Find the anime by ID
        const anime = await AnimeModel.findById(animeId);

        if (!anime) {
            return res.status(404).json({ message: 'Anime not found' });
        }

        // Update the current episode
        anime.currentEpisode = currentEpisode;
        if(status==="Planning"){
                // Update the status based on the current episode
            if (currentEpisode === anime.episodes && anime.status !== 'Completed') {
                anime.status = 'Completed';
            } else if (currentEpisode > 0 && anime.status === 'Planning') {
                anime.status = 'Watching';
            }
        }else if(status==="Completed"){
            anime.status = status;
            anime.currentEpisode = anime.episodes;
        }

        

        // Save the updated anime
        await anime.save();

        res.json({ message: 'Status updated successfully' });
    } catch (error) {
        console.error('Failed to update status:', error);
        res.status(500).json({ message: 'Internal Server Error' });
    }
});



/*=================================
        get and post
===================================*/
app.post("/register", async (req, res) => {
    console.log(req.body);
    const { firstName, lastName, email, password } = req.body;

    try {
        const user = await UserModel.findOne({ email: email });

        if (user) {
            res.send({ message: "This email id already registered" });
        } else {
            const newUser = new UserModel({
                firstName,
                lastName,
                email,
                password,
            });

            await newUser.save();
            res.send({ message: "Successfully registered" });
        }
    } catch (error) {
        console.error(error);
        res.status(500).send({ message: "Internal Server Error" });
    }
});

app.post("/login", async (req, res) => {
    console.log(req.body);
    const { email, password } = req.body;

    try {
        const user = await UserModel.findOne({ email: email });

        if (!user) {
            return res.status(404).json({ message: "This email id is not registered" });
        }

        if (password === user.password) {
            return res.json({ message: "Login Successful", user });
        } else {
            return res.status(401).json({ message: "Password didn't match" });
        }
    } catch (error) {
        console.error(error);
        return res.status(500).json({ message: "Internal Server Error" });
    }
});

app.get('/browse', async (req, res) => {
    try {
        const animes = await AnimeModel.find({});
        console.log("Animes: ", animes);
        res.json(animes);
    } catch (error) {
        console.error("Error fetching animes:", error);
        res.status(500).json({ message: 'Internal Server Error' });
    }    
});


app.post("/addanime", async (req, res) => {
    console.log('Received request to create anime:', req.body);
    try {
        
        

        // Validate
        const { title, genres, episodes, image, description, characters, status } = req.body;
        if(!title) {
        console.log(title);
        return res.status(400).json({message: 'no title'});
        }
        // Convert the genres string to an array of objects
        const genresArray = genres.map(genre => ({ genre }));

        if (!genresArray || genresArray.length === 0 || !genresArray[0].genre) {
        console.log(genresArray);
        return res.status(400).json({ message: 'genres issue' });
        }
        if( !episodes) {
        console.log(episodes);
        return res.status(400).json({message: 'no episode'});
        }
        const charactersArray = characters.split(',').map(name => ({ name }));

        if (!charactersArray || charactersArray.length === 0 || !charactersArray[0].name) {
        console.log(charactersArray);
        return res.status(400).json({ message: 'characters issue' });
        }

        const anime = await AnimeModel.create({
        title,
        genres: genresArray,
        episodes,
        image,
        description,
        characters: charactersArray,
        status
        });

        res.status(201).json(anime);

    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

/*============================
        listen
=============================*/
app.listen(8080,()=>{
    console.log("Server is runing at port 8080")
})