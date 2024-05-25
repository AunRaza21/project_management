document.addEventListener('DOMContentLoaded', function () {
    const chatLog = document.querySelector('#chat-log');
    if (chatLog) {
        chatLog.scrollTop = chatLog.scrollHeight;  // Scroll to the bottom

        const chatForm = document.querySelector('#chat-form');
        const chatSocket = new WebSocket(
            'ws://' + window.location.host + '/ws/chat/' + chatForm.dataset.roomName + '/'
        );

        chatSocket.onmessage = function (e) {
            const data = JSON.parse(e.data);
            chatLog.value += (data.message + '\n');
            chatLog.scrollTop = chatLog.scrollHeight;  // Scroll to the bottom
        };

        chatSocket.onclose = function (e) {
            console.error('Chat socket closed unexpectedly');
        };

        chatForm.onsubmit = function (e) {
            e.preventDefault();
            const messageInputDom = document.querySelector('#chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';
        };
    }
});
