var Schema = require('mongoose').Schema;

var Startup = new Schema({
  name: String,
  preferences: String
});

module.exports = Startup;
