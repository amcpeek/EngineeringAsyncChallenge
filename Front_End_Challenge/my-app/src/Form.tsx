import React, { useState } from "react";

const Form = () => {
  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const newUser = { name, email, industry };
    console.log(newUser);
  };

  const [name, setName] = useState<string>("");
  const [email, setEmail] = useState<string>("");
  const [industry, setIndustry] = useState<string>("E-Sports");
  const allIndustries: string[] = [
    "E-Sports",
    "Spots/Fitness",
    "Professional Services",
  ];
  return (
    <div>
      <div className="b-green center classroom-background">
        <div className="join-mailing">Join our mailing list</div>
        <div className="outer-gray">
          <form onSubmit={handleSubmit}>
            <div className="b-red row background-gray">
              <div className="b-orange outer-form">
                <div className="form-format">
                  <div className="purple">Full Name</div>
                  <label>
                    <input
                      type="text"
                      name="name"
                      required
                      value={name}
                      onChange={(
                        event: React.ChangeEvent<HTMLInputElement>
                      ) => {
                        setName(event.target.value);
                      }}
                    />
                  </label>
                  <div>Email</div>
                  <label>
                    <input
                      type="email"
                      name="email"
                      value={email}
                      required
                      onChange={(
                        event: React.ChangeEvent<HTMLInputElement>
                      ) => {
                        setEmail(event.target.value);
                      }}
                    />
                  </label>
                  <div>Industry</div>
                  <label>
                    <select
                      placeholder="State"
                      value={industry}
                      onChange={(
                        event: React.ChangeEvent<HTMLSelectElement>
                      ) => {
                        setIndustry(event.target.value);
                      }}
                    >
                      {allIndustries.map((state) => (
                        <option key={state} value={state}>
                          {" "}
                          {state}
                        </option>
                      ))}
                    </select>
                  </label>
                </div>
              </div>

              <div className="b-green center join-right">
                <div className="join-text">
                  Join our mailing to receive notifications about program
                  availability and special discounts
                </div>
                <div className="">
                  <button className="reg-button" type="submit">
                    Sign Up Fix
                  </button>
                </div>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Form;
