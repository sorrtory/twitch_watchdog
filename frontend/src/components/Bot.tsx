import React from "react";
import api from "../api";
interface BotProps {
    title: string;
    members_count: string;
    photo: string;
}

const Bot: React.FC<BotProps> = ({ title, members_count, photo }) => {
  const handleClick = () => {
    // Send a test message to the bot
    api.post("/send_message", { message: "Test message from WatchDog" })
        .then(response => {
            console.log("Message sent successfully:", response.data);
        })
        .catch(error => {
            console.error("Error sending message:", error);
        });
  };
  return (
    <>
        <img
            src={photo}
            alt="Chat Avatar"
            className="sm:w-16 sm:h-16 w-12 h-12 mx-auto"
          />
        <p>
        &#x0022;
        <span className="text-primaryTextColor dark:text-primaryTextColor-dark truncate overflow-hidden whitespace-nowrap">
          {title}
        </span>
        &#x0022;
      </p>
      <button
        className={`cursor-pointer bg-transparent font-bold hover:underline ${
          members_count == "-1" ? "text-errorColor" : "text-successColor"
        }`}
        type="button"
        title="Click to send a test message"
        onClick={handleClick}
      >
        {members_count}
      </button>
    </>
  );
};

export default Bot;
export type { BotProps };
