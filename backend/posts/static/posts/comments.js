'use strict';

(function(global) {
    const comments = document.querySelector('.comments');
    const commentTextInput = document.querySelector('.comment-text-input');

    comments.addEventListener('click', (event) => {
        if (event.target.className !== 'comment-author-name') {
            return;
        }

        const userName = event.target.innerText;

        if (!commentTextInput.value) {
            commentTextInput.value = `@${userName}, `;
        } else {
            commentTextInput.value += `@${userName} `;
        }
    })
}) (window)
