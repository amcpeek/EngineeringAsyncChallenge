import React from "react";
import BL_LogoBasic from "./media/BL_LogoBasic.png";
import Hero from "./media/hero.png"

import "./App.css";

function App() {
  return (
    <div className="center column">
      <div className="b-blue hero-background">
        <div className="b-red column jc-start margin-10-vw">
          <img
            src={BL_LogoBasic}
            alt="Better Lesson Logo"
            className="logo"
          ></img>
          <h1 className='font-5em white'>BetterLesson <br/> Professional Coaching</h1>
          <div className='font-2-4em white'>PROFESSIONAL COACH SEMINARS & MENTORSHIP</div>
        </div>
        <div className="b-orange margin-10-vw-lr jc-start">
          <button className='reg-button'>Register Now</button>
        </div>
      </div>

      <div className="b-orange row center ">
        <div className="b-green coach-background"></div>
        <div className="b-blue currentCoachesRight">
           <div className='currentCoachesTitle b-green'>Current Coaches</div>

          <div className='table-container'>
            <div className='table-headers'>
              <div className='trow'>Coach Name</div>
              <div className='trow-m'>Available <br/> Starting</div>
              <div className='trow-e'>Industry</div>
            </div>
            <div className='table-row'>
              <div className='trow'>Jessica D.</div>
              <div className='trow-m'>11/6/22 </div>
              <div className='trow-e'>Professional Services</div>
            </div>
            <div className='table-row'>
              <div className='trow'>David F.</div>
              <div className='trow-m'>8/5/21</div>
              <div className='trow-e'>Sports/Fitness</div>
            </div>
            <div className='table-row'>
              <div className='trow'>Keir Y.</div>
              <div className='trow-m'>4/12/22</div>
              <div className='trow-e'>E-Sports</div>
            </div>
          </div>


        </div>
      </div>
      <div className="b-green center classroom-background">
        <div className='join-mailing'>Join our mailing list</div>
        <div className='outer-gray'>
        <div className="b-red row background-gray">
          <div className="b-orange outer-form">Form: Full Name Email Industry</div>
          <div className="b-green center join-right">
            <div className='join-text'>
              Join our mailing to receive notifications about program
              availability and special discounts
            </div>
            <div className="">
          <button className='reg-button'>Sign Up</button>
        </div>
          </div>
        </div>

        </div>

      </div>


      <div className="b-blue row center bottom-info">
        <div>
          <div className='font-larger'>EMAIL ADDRESS</div>
          <div>hello@reallygreatsite.com</div>
        </div>

        <div>
          <div className='font-larger'>MAILING ADDRESS</div>
          <div>123 Anywhere St. Any City, ST 12345</div>
        </div>

        <div>
          <div className='font-larger'>PHONE NUMBER</div>
          <div>(123) 456-7890</div>
        </div>
      </div>
    </div>
  );
}

export default App;
