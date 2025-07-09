def test_send_message():
    from src.vk import VKBot
    from src.config import VK_WRITE_TO
    from datetime import datetime

    bot = VKBot()
    msg = f"Test message at {datetime.now()}"   # Create a test message
    peer_id = 2000000000 + int(VK_WRITE_TO[0])  # Convert group ID to peer_id
    # Test sending a message
    response = bot.send_message(msg, peer_id)
    assert response is not False
    