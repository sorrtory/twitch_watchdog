import React from "react";

const Home: React.FC = () => {
  const handleRequest = () => {
    // Handle request logic here
    console.log("Request sent");
  };
  const handleAutoRequestToggle = (
    event: React.ChangeEvent<HTMLInputElement>,
  ) => {
    // Handle auto request toggle logic here
    console.log("Auto request toggled:", event.target.checked);
    const checkButton = document.getElementById(
      "check-button",
    ) as HTMLButtonElement | null;
    if (checkButton) {
      checkButton.disabled = event.target.checked;
      checkButton.classList.toggle("opacity-50", event.target.checked);
      checkButton.classList.toggle("cursor-not-allowed", event.target.checked);
      checkButton.classList.toggle("cursor-pointer", !event.target.checked);
    }
  };
  return (
    <section className="container flex flex-wrap items-center justify-center gap-3">
      <article className="card">
        <h2>Twitch</h2>

        <div className="grid grid-cols-2 gap-2">
          <p>Streamer</p>
          <span className="text-primaryTextColor dark:text-primaryTextColor-dark font-bold">
            merelley
          </span>
          <p>Status</p>
          <span className="text-successColor font-bold">Online</span>
        </div>
        <hr className="border-mutedTextColor mt-2" />
        <div className="mt-5">
          <p className="text-mutedTextColor">Last check: 2023-10-01 12:00:00</p>
        </div>
        <div className="mt-2 flex items-center space-x-3">
          <button
            className="btn-primary cursor-pointer"
            onClick={handleRequest}
            id="check-button"
          >
            Check
          </button>
          <label className="inline-flex cursor-pointer items-center">
            <input
              type="checkbox"
              className="peer sr-only"
              onChange={handleAutoRequestToggle}
            />
            <div className="toggle-primary"></div>
            <span className="ml-1 text-sm font-medium">Auto check</span>
          </label>
        </div>
      </article>
    </section>
  );
};

export default Home;
