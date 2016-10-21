var express = require('express');
var app = express();
var mongoose = require('mongoose');
var bodyParser = require('body-parser');

// Mongoose
var conn = mongoose.connect('mongodb://localhost/scheduling');
var Investor = conn.model('Investor', require('./models/Investor'));
var Startup = conn.model('Startup', require('./models/Startup'));

// Views Setup
app.set('view engine', 'pug');
app.use(express.static('public'));

// Endpoints
app.use(bodyParser());
app.get('/', function (req, res) {
  res.render('index', { title: 'Schedule', message: 'Schedule' });
});

app.post('/', function (req, res) {
  console.log(req.body);
  res.redirect('/');
});

app.get('/investors', function (req, res) {
  Investor.find({}, function (error, investors) {
    if (error) console.log(error);
    res.render('investors', {
      title: 'Investors',
      message: 'Investors',
      investors: investors
    });
  });
});

app.post('/investors', function (req, res) {
  console.log(req.body);
  new Investor(req.body).save(function (error, result) {
    if (error) console.log(error);
    res.redirect('/investors');
  });
});

app.get('/startups', function (req, res) {
  Startup.find({}, function (error, startups) {
    console.log(startups);
    if (error) console.log(error);
    res.render('startups', {
      title: 'Startups',
      message: 'Startups',
      startups: startups
    });
  });
});

app.post('/startups', function (req, res) {
  console.log(req.body);
  new Startup(req.body).save(function (error, result) {
    if (error) console.log(error);
    res.redirect('/startups');
  });
});

app.listen(3000, function () {
  console.log('Scheduling service listening on port 3000!');
});
