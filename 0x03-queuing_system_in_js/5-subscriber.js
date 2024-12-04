import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

// Subscribe to the channel
client.subscribe('holberton school channel');

// Handle messages
client.on('message', (channel, message) => {
  console.log(`Received message: ${message} on channel: ${channel}`);
  if (message === 'KILL_SERVER') {
    client.unsubscribe('holberton school channel');
    client.quit();
  }
});
