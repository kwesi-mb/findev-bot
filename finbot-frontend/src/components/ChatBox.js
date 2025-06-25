import React, { useState } from 'react';
import axios from 'axios';

const ChatBox = () => {
    const [messages, setMessages] = useState([]);
    const [userInput, setUserInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleSend = async () => {
        if (!userInput.trim()) return;

        const newMessages = [...messages, { sender: 'user', text: userInput }];
        setMessages(newMessages);
        setUserInput('');
        setIsLoading(true);

        try {
            const res = await axios.post('http://localhost:8000/chat', {
                message: userInput
            });

            setMessages([
                ...newMessages,
                { sender: 'bot', text: res.data.reply }
            ]);
        } catch (err) {
            console.error('Error communicating with FinBot:', err);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div style={{ maxWidth: 600, margin: '2rem auto' }}>
            <h2>FinBot - Financial Advice Chat</h2>
            <div style={{
                border: '1px solid #ccc',
                padding: '1rem',
                height: '400px',
                overflowY: 'auto',
                marginBottom: '1rem',
                borderRadius: '8px'
            }}>
                {messages.map((msg, idx) => (
                    <div key={idx} style={{ margin: '0.5 rem 0', textAlign: msg.sender === 'user' ? 'right' : 'left' }}>
                        <strong>{msg.sender === 'user' ? 'You' : 'FinBot'}:</strong> {msg.text}
                    </div>
                ))}
            </div>
            <input
                type = "text"
                placeholder="Ask a financial question..."
                value={userInput}
                onChange={e => setUserInput(e.target.value)}
                style={{ width: '75%', padding: '0.5rem' }}
            />
            <button onClick={handleSend} disabled={isLoading} style={{ padding: '0.5rem', marginLeft: '0.5rem' }}>
                {isLoading ? 'Thinking...' : 'Send'}
            </button>
        </div>
    );
};

export default ChatBox;