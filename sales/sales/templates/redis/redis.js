const redis = require('redis');

const client = redis.createClient({
  host: 'localhost',
  port: 6379,
});

// error handling
client.on('error', (err) => {
  console.error('Redis connection error:', err);
});

// setter
const setKey = (key, value) => {
  client.set(key, value, (err) => {
    if (err) {
      console.error('Error setting key:', err);
    }
  });
};

// getter
const getValue = (key) => {
  return new Promise((resolve, reject) => {
    client.get(key, (err, value) => {
      if (err) {
        reject(err);
      } else {
        resolve(value);
      }
    });
  });
};

// connection cleanup
process.on('SIGINT', () => {
  client.quit();
  process.exit();
});