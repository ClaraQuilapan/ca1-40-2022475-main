// load.js: reads a JSON file and loads its contents into MongoDB

const fs = require('fs');

// Read the contents of 'ph_averages.json', one JSON object per line
const docs = fs.readFileSync('ph_averages.json', 'utf8')
               .trim()
               .split('\n')          // Split into lines
               .map(JSON.parse);     // Parse each line as a JSON object

// Connect to MongoDB
const client = new Mongo();
const db = client.getDB('waterdb');

// Drop the existing 'ph_averages' collection (optional, for a fresh load)
db.ph_averages.drop();

// Create a new collection named 'ph_averages'
db.createCollection('ph_averages');

// Insert all parsed documents into the collection
db.ph_averages.insertMany(docs);

// Print a summary message to the shell
print('Inserted', docs.length, 'documents');