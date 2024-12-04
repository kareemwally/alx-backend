import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

const queue = kue.createQueue();

const jobs = [
  { phoneNumber: '4153518780', message: 'This is the code 1234' },
  { phoneNumber: '4153518781', message: 'This is the code 4562' },
  { phoneNumber: '4153518743', message: 'This is the code 4321' },
  { phoneNumber: '4153538781', message: 'This is the code 4562' },
  { phoneNumber: '4153118782', message: 'This is the code 4321' },
  { phoneNumber: '4153718781', message: 'This is the code 4562' },
  { phoneNumber: '4159518782', message: 'This is the code 4321' },
  { phoneNumber: '4158718781', message: 'This is the code 4562' },
  { phoneNumber: '4153818782', message: 'This is the code 4321' },
  { phoneNumber: '4154318781', message: 'This is the code 4562' },
  { phoneNumber: '4151218782', message: 'This is the code 4321' }
];

createPushNotificationsJobs(jobs, queue);
