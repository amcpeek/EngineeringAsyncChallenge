import React from 'react';

import './App.css';

function App() {
  return (
    <div className='center column'>
      <div className='b-red column'>
      <div>Logo</div>
      <div>Better Lesson</div>
      <div>Professional Coaching</div>
      <div>Professional Coach Seminars & Mentorship</div>
      <button>Register Now</button>
      </div>

      <div className='b-orange row center'>
        <div className='left b-green'>img</div>
        <div className='right b-blue'>
          <div>Current Coaches</div>
          <div>Coach Name, Available Starting, Industry</div>
          <div>Jessica D. 11/6/22 Professional Services</div>
          <div>David F. 8/5/21 Sports/Fitness</div>
          <div>Keir Y. 4/12/22 E-Sports</div>
        </div>
      </div>
      <div className='b-green center'>
        <div>Join our mailing list</div>
        <div className='b-red row'>
          <div className='b-orange'>
            Form:
            Full Name
            Email
            Industry
          </div>
          <div className='b-green center'>
            <div>Join our mailing to receive notifications about program availability and special discounts</div>
            <button>Sign Up</button>

          </div>
        </div>
      </div>
      <div className='b-blue row center'>
        <div>
          <div>Email Address</div>
          <div>hello@reallygreatsite.com</div>
        </div>

        <div>
          <div>Mailing Address</div>
          <div>123 Anywhere St. Any City, ST 12345</div>
        </div>

        <div>
          <div>Phone Number</div>
          <div>(123) 456-7890</div>
        </div>
      </div>


    </div>
  );
}

export default App;
