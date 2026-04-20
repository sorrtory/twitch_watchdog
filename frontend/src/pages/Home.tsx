import React from "react";
import { useEffect, useState } from "react";
import api from "../api";

const Home: React.FC = () => {
  const [status, setStatus] = useState("Loading...");
  const [lastCheck, setLastCheck] = useState("Loading...");

  const fetchStreamStatus = async () => {
    setStatus("Loading...");
    setLastCheck("Loading...");
    api
      .get("/get_stream_status/")
      .then((response) => {
        setStatus(response.data.is_alive ? "Online" : "Offline");
        setLastCheck(response.data.last_check);
      })
      .catch((error) => {
        console.error("Error fetching Twitch status:", error);
      });
  };

  useEffect(() => {
    fetchStreamStatus();
  }, []);

  const handleAutoRequestToggle = (
    event: React.ChangeEvent<HTMLInputElement>,
  ) => {
    const checkButton = document.getElementById(
      "check-button",
    ) as HTMLButtonElement | null;
    if (checkButton) {
      checkButton.disabled = event.target.checked;
      checkButton.classList.toggle("opacity-50", event.target.checked);
      checkButton.classList.toggle("cursor-not-allowed", event.target.checked);
      checkButton.classList.toggle("cursor-pointer", !event.target.checked);
    }

    if (event.target.checked) {
      const intervalId = setInterval(() => {
        fetchStreamStatus();
      }, 5000);
      return () => clearInterval(intervalId);
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
          <span
            className={` ${status === "Online" ? "text-successColor" : "text-errorColor"} font-bold`}
          >
            {status}
          </span>
        </div>
        <hr className="border-mutedTextColor mt-2" />
        <div className="mt-5 text-mutedTextColor">
          <p className="flex justify-around items-center gap-2">
            <span>Last check:</span>
            <span className="font-bold">{lastCheck}</span>
          </p>
        </div>
        <div className="mt-2 flex items-center space-x-3">
          <button
            className="btn-primary cursor-pointer"
            onClick={fetchStreamStatus}
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
