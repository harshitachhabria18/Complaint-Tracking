// Toggle chatbot window
document.querySelector('.chatbot').addEventListener('click', function () {
    const chatWindow = document.querySelector('.chat-window');
    chatWindow.style.display = chatWindow.style.display === 'flex' ? 'none' : 'flex';
});

document.querySelector('.close-chat').addEventListener('click', function () {
    document.querySelector('.chat-window').style.display = 'none';
});

// FAQ question click handler
document.querySelectorAll('.faq-question').forEach(button => {
    button.addEventListener('click', function () {
        const question = this.textContent;
        const chatMessages = document.querySelector('.chat-messages');

        // Add user question
        const userMessage = document.createElement('div');
        userMessage.className = 'd-flex justify-content-end mb-2';
        userMessage.innerHTML = `
                    <div class="bg-primary text-white p-2 rounded" style="max-width: 70%;">
                        ${question}
                    </div>
                `;
        chatMessages.appendChild(userMessage);

        // Add bot response
        setTimeout(() => {
            const botMessage = document.createElement('div');
            botMessage.className = 'd-flex justify-content-start mb-2';

            let response = '';
            if (question.includes('submit')) {
                response = 'To submit a new complaint, click on "New Complaint" in the sidebar. Fill out the form with details about your issue, add any evidence images, and choose whether to remain anonymous. Click submit when done.';
            } else if (question.includes('status')) {
                response = 'You can check your complaint status in the "Recent Complaints" table on your dashboard. The status column shows whether your complaint is pending, in progress, or resolved.';
            } else if (question.includes('unresolved')) {
                response = 'If your complaint remains unresolved for a long time, you can send a message to the concerned department from the complaint details page. You can also escalate the issue by contacting student support.';
            } else {
                response = 'I understand you need help with: ' + question + '. Please contact our support team at support@university.edu for further assistance.';
            }

            botMessage.innerHTML = `
                        <div class="bg-light p-2 rounded" style="max-width: 70%;">
                            ${response}
                        </div>
                    `;
            chatMessages.appendChild(botMessage);
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }, 500);
    });
});

// Initialize tooltips
const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});

// Show complaint detail modal when view buttons are clicked
document.querySelectorAll('.btn-outline-primary').forEach(button => {
    if (button.textContent.trim() === 'View') {
        button.addEventListener('click', function () {
            const modal = new bootstrap.Modal(document.getElementById('complaintDetailModal'));
            modal.show();
        });
    }
});
