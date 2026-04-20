import React from "react";
import Bot from "../components/Bot";
import type { BotProps } from "../components/Bot";
import { useEffect, useState } from "react";
import api from "../api";

const Bots: React.FC = () => {
  const [data, setData] = useState<BotProps[]>([]);
  const [loading, setLoading] = useState(true);


  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await api.get("/get_chats");
        console.log("Chats:", response.data.chats);
        console.log("Response:", response.data.chats[0]);
        setData(response.data.chats || []);
      } catch (error) {
        console.error("Error fetching chats:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <p className="text-mutedTextColor text-center">Loading...</p>;
  }
  if (data.length === 0) {
    return (
      <p className="text-mutedTextColor text-center">No chats available.</p>
    );
  }

  return (
    <section className="container flex flex-col items-center justify-center gap-3">
      <article className="card">
        <h2>VK chats</h2>
        <div className="grid grid-cols-[1fr_auto_1fr] gap-2 text-center items-center justify-center">
          <p className="font-bold">Chat Image</p>
          <p className="font-bold">Chat Name</p>
          <p className="font-bold">People</p>
          {data &&
            data.length > 0 &&
            data.map((chat: BotProps, idx: number) => (
              <Bot
                key={idx}
                title={chat.title}
                members_count={chat.members_count}
                photo={chat.photo}
              />
            ))}
        </div>
        <hr className="border-mutedTextColor mt-5" />
        <form action="" className="grid justify-items-center">
          <textarea name="" id="" className="input-primary mt-2"></textarea>
          <button
            type="submit"
            className="btn-primary mt-2 w-3/4 cursor-pointer"
          >
            Save
          </button>
        </form>
      </article>
      <article className="card">
        <h2>Telegram channel</h2>
        <p className="text-mutedTextColor text-center">...</p>
      </article>
      <article className="card">
        <h2>VK public</h2>
        <p className="text-mutedTextColor text-center">...</p>
      </article>
    </section>
  );
};

export default Bots;
