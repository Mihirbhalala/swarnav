/**
 * Swarnav Tour & Travels - Main Interactive JavaScript
 * Includes: Navigation Dropdowns, Regional Tour Filter Tabs,
 * Quick Inquiry Modal, Interactive AI Pilgrimage Assistant, and WhatsApp Integration.
 */

document.addEventListener('DOMContentLoaded', () => {
    // --------------------------------------------------------------------------
    // 1. Mobile Navigation & Header Dropdown Toggles
    // --------------------------------------------------------------------------
    const navToggle = document.getElementById('nav-toggle');
    const primaryNav = document.getElementById('primary-nav');
    const toursMenuItem = document.getElementById('tours-menu-item');
    const toursDropdownBtn = toursMenuItem ? toursMenuItem.querySelector('.nav-dropdown-btn') : null;

    if (navToggle && primaryNav) {
        navToggle.addEventListener('click', () => {
            const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
            navToggle.setAttribute('aria-expanded', String(!isExpanded));
            primaryNav.classList.toggle('is-active');
        });

        // Mobile dropdown click toggle
        if (toursDropdownBtn && toursMenuItem) {
            toursDropdownBtn.addEventListener('click', (e) => {
                if (window.innerWidth < 992) {
                    e.preventDefault();
                    toursMenuItem.classList.toggle('is-open');
                    const isDropdownOpen = toursMenuItem.classList.contains('is-open');
                    toursDropdownBtn.setAttribute('aria-expanded', String(isDropdownOpen));
                }
            });
        }

        // Close menu on ESC key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (primaryNav.classList.contains('is-active')) {
                    primaryNav.classList.remove('is-active');
                    navToggle.setAttribute('aria-expanded', 'false');
                    navToggle.focus();
                }
                closeAiModal();
                closeInquiryModal();
            }
        });

        // Close mobile menu when navigating to anchor
        const navLinks = primaryNav.querySelectorAll('a[href*="#"]');
        navLinks.forEach((link) => {
            link.addEventListener('click', () => {
                if (window.innerWidth < 992) {
                    primaryNav.classList.remove('is-active');
                    navToggle.setAttribute('aria-expanded', 'false');
                }
            });
        });
    }

    // --------------------------------------------------------------------------
    // 2. Homepage Tour Category Filter Tabs
    // --------------------------------------------------------------------------
    const filterTabs = document.querySelectorAll('.filter-tab');
    const tourCards = document.querySelectorAll('.tour-card');

    if (filterTabs.length > 0 && tourCards.length > 0) {
        filterTabs.forEach((tab) => {
            tab.addEventListener('click', () => {
                filterTabs.forEach(t => {
                    t.classList.remove('active');
                    t.setAttribute('aria-selected', 'false');
                });
                tab.classList.add('active');
                tab.setAttribute('aria-selected', 'true');

                const filterValue = tab.getAttribute('data-filter');

                tourCards.forEach((card) => {
                    const cardCategory = card.getAttribute('data-category');
                    if (filterValue === 'all' || cardCategory === filterValue) {
                        card.style.display = 'flex';
                        card.style.opacity = '0';
                        setTimeout(() => {
                            card.style.opacity = '1';
                        }, 20);
                    } else {
                        card.style.display = 'none';
                    }
                });
            });
        });
    }

    // --------------------------------------------------------------------------
    // 3. Quick Inquiry Modal Handling
    // --------------------------------------------------------------------------
    const inquiryModal = document.getElementById('inquiry-modal-overlay');
    const closeInquiryBtn = document.getElementById('close-inquiry-modal-btn');
    const openInquiryBtns = document.querySelectorAll('.open-inquiry-btn');
    const modalTourSelect = document.getElementById('modal-tour-select');

    function openInquiryModal(tourName) {
        if (!inquiryModal) return;
        inquiryModal.classList.add('is-active');
        inquiryModal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('modal-open');

        if (tourName && modalTourSelect) {
            // Find best matching option by value or text
            const searchVal = tourName.toLowerCase();
            let matched = false;
            for (let i = 0; i < modalTourSelect.options.length; i++) {
                const opt = modalTourSelect.options[i];
                if (opt.value && (opt.value.toLowerCase() === searchVal || opt.text.toLowerCase().includes(searchVal) || searchVal.includes(opt.value.toLowerCase()))) {
                    modalTourSelect.selectedIndex = i;
                    matched = true;
                    break;
                }
            }
            if (!matched && modalTourSelect.options.length > 1) {
                modalTourSelect.selectedIndex = 1; // Default to Char Dham
            }
        }
    }

    function closeInquiryModal() {
        if (!inquiryModal) return;
        inquiryModal.classList.remove('is-active');
        inquiryModal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('modal-open');
    }

    openInquiryBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const tourName = btn.getAttribute('data-tour') || '';
            openInquiryModal(tourName);
        });
    });

    if (closeInquiryBtn) {
        closeInquiryBtn.addEventListener('click', closeInquiryModal);
    }

    if (inquiryModal) {
        inquiryModal.addEventListener('click', (e) => {
            if (e.target === inquiryModal) {
                closeInquiryModal();
            }
        });
    }


    // --------------------------------------------------------------------------
    // 4. Interactive AI Pilgrimage Assistant
    // --------------------------------------------------------------------------
    const aiModal = document.getElementById('ai-modal-overlay');
    const openAiBtn = document.getElementById('open-ai-assistant-btn');
    const floatingAiTrigger = document.getElementById('floating-ai-trigger');
    const closeAiBtn = document.getElementById('close-ai-modal-btn');
    const aiChatMessages = document.getElementById('ai-chat-messages');
    const aiChatForm = document.getElementById('ai-chat-form');
    const aiUserInput = document.getElementById('ai-user-input');
    const aiChips = document.querySelectorAll('.ai-chip');

    function openAiModal() {
        if (!aiModal) return;
        aiModal.classList.add('is-active');
        aiModal.setAttribute('aria-hidden', 'false');
        document.body.classList.add('modal-open');
        if (aiUserInput) {
            setTimeout(() => aiUserInput.focus(), 150);
        }
    }

    function closeAiModal() {
        if (!aiModal) return;
        aiModal.classList.remove('is-active');
        aiModal.setAttribute('aria-hidden', 'true');
        document.body.classList.remove('modal-open');
    }

    if (openAiBtn) openAiBtn.addEventListener('click', openAiModal);
    if (floatingAiTrigger) floatingAiTrigger.addEventListener('click', openAiModal);
    if (closeAiBtn) closeAiBtn.addEventListener('click', closeAiModal);
    if (aiModal) {
        aiModal.addEventListener('click', (e) => {
            if (e.target === aiModal) closeAiModal();
        });
    }

    // --------------------------------------------------------------------------
    // Advanced RAG & Agentic AI Assistant Client (Gemini 2.5/1.5 Flash + Tool Calling)
    // --------------------------------------------------------------------------
    const resetAiBtn = document.getElementById('ai-reset-chat-btn');
    const aiSuggestionsChips = document.getElementById('ai-suggestions-chips');
    const aiSubmitBtn = document.getElementById('ai-send-submit-btn');

    function getAiCsrfToken() {
        let cookieValue = '';
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith('csrftoken=')) {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue || document.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
    }

    // Markdown Formatter for Rich AI Responses
    function formatMarkdownText(text) {
        if (!text) return '';
        let html = text
            // Escape special HTML chars except existing intentional tags
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');

        // Bold (**text**)
        html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        // Italic (*text*)
        html = html.replace(/\*([^*\n]+)\*/g, '<em>$1</em>');

        // Split into lines to format lists
        const lines = html.split('\n');
        let inList = false;
        let formattedLines = [];

        for (let i = 0; i < lines.length; i++) {
            let line = lines[i].trim();
            if (line.startsWith('• ') || line.startsWith('- ') || line.startsWith('* ')) {
                if (!inList) {
                    formattedLines.push('<ul class="ai-response-list">');
                    inList = true;
                }
                formattedLines.push(`<li>${line.substring(2)}</li>`);
            } else {
                if (inList) {
                    formattedLines.push('</ul>');
                    inList = false;
                }
                if (line) {
                    formattedLines.push(`<p>${line}</p>`);
                }
            }
        }
        if (inList) {
            formattedLines.push('</ul>');
        }

        return formattedLines.join('');
    }

    function appendMessage(sender, content, isFormattedHtml = false) {
        if (!aiChatMessages) return;
        const msgDiv = document.createElement('div');
        msgDiv.className = `ai-msg ai-msg-${sender}`;

        const bubble = document.createElement('div');
        bubble.className = 'ai-bubble';

        if (isFormattedHtml) {
            bubble.innerHTML = content;
        } else if (sender === 'user') {
            bubble.textContent = content;
        } else {
            bubble.innerHTML = formatMarkdownText(content);
        }

        msgDiv.appendChild(bubble);
        aiChatMessages.appendChild(msgDiv);
        aiChatMessages.scrollTop = aiChatMessages.scrollHeight;
    }

    function appendActionCard(card) {
        if (!aiChatMessages || !card) return;
        if (card.type === 'lead_created') {
            const cardDiv = document.createElement('div');
            cardDiv.className = 'ai-msg ai-msg-bot';
            cardDiv.innerHTML = `
                <div class="ai-action-card">
                    <div class="ai-action-badge">✨ Booking Lead Confirmed</div>
                    <h4 class="ai-action-ref">Inquiry Reference: ${card.inquiry_ref || 'SW-INQ'}</h4>
                    <p class="ai-action-text">Your inquiry has been successfully registered in our system. Our senior tour coordinator is preparing your customized yatra package.</p>
                    ${card.whatsapp_link ? `
                        <a href="${card.whatsapp_link}" target="_blank" rel="noopener noreferrer" class="ai-action-wa-btn">
                            <svg viewBox="0 0 24 24" width="20" height="20" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2M12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.15 12.04 20.15C10.56 20.15 9.11 19.76 7.85 19.01L7.55 18.83L4.43 19.65L5.26 16.61L5.06 16.29C4.24 14.99 3.8 13.47 3.8 11.91C3.81 7.37 7.5 3.67 12.05 3.67Z"/></svg>
                            <span>Open in WhatsApp &amp; Confirm Booking</span>
                        </a>
                    ` : ''}
                </div>
            `;
            aiChatMessages.appendChild(cardDiv);
            aiChatMessages.scrollTop = aiChatMessages.scrollHeight;
        }
    }

    function updateSuggestionChips(suggestions) {
        const container = aiSuggestionsChips || document.querySelector('.suggestions-chips');
        if (!container || !suggestions || !suggestions.length) return;

        container.innerHTML = '';
        suggestions.forEach(prompt => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'ai-chip';
            btn.setAttribute('data-prompt', prompt);
            btn.textContent = prompt;
            btn.addEventListener('click', () => {
                processAiQuery(prompt);
            });
            container.appendChild(btn);
        });
    }

    async function processAiQuery(query) {
        const trimmed = (query || '').trim();
        if (!trimmed) return;

        // Render user message immediately
        appendMessage('user', trimmed);

        // Lock form during generation
        if (aiUserInput) aiUserInput.value = '';
        if (aiSubmitBtn) aiSubmitBtn.disabled = true;

        // Show typing pulse indicator
        const typingDiv = document.createElement('div');
        typingDiv.className = 'ai-msg ai-msg-bot typing-indicator';
        typingDiv.innerHTML = `
            <div class="ai-bubble">
                <span class="ai-typing-dots"><span></span><span></span><span></span></span>
                <em>Consulting Swarnav Yatra RAG knowledge base...</em>
            </div>
        `;
        aiChatMessages.appendChild(typingDiv);
        aiChatMessages.scrollTop = aiChatMessages.scrollHeight;

        try {
            const csrfToken = getAiCsrfToken();
            const response = await fetch('/api/ai/chat/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken,
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: JSON.stringify({ message: trimmed })
            });

            const data = await response.json();
            typingDiv.remove();

            if (data.success && data.reply) {
                appendMessage('bot', data.reply);
                if (data.action_card) {
                    appendActionCard(data.action_card);
                }
                if (data.suggested_questions && data.suggested_questions.length) {
                    updateSuggestionChips(data.suggested_questions);
                }
            } else {
                appendMessage('bot', (data && data.error) ? data.error : "I apologize, I could not complete that request. Please contact our team directly at +91 95868 25353.");
            }
        } catch (err) {
            console.error("AI Assistant API error:", err);
            typingDiv.remove();
            appendMessage('bot', `🙏 Thank you for your question regarding <strong>"${trimmed}"</strong>.<br><br>
                Swarnav Tour & Travels offers personalized assistance for Char Dham, Panch Kedar, Kashmir, South India, Jagannath Puri, and Nepal.<br><br>
                For batch schedules or custom departure dates, connect directly with our coordination team at <strong>+91 95868 25353</strong> or on WhatsApp.`);
        } finally {
            if (aiSubmitBtn) aiSubmitBtn.disabled = false;
            if (aiUserInput) {
                setTimeout(() => aiUserInput.focus(), 100);
            }
        }
    }

    // Handle Form Submit
    if (aiChatForm && aiUserInput) {
        aiChatForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const q = aiUserInput.value;
            processAiQuery(q);
        });
    }

    // Reset Chat Session Handler
    if (resetAiBtn) {
        resetAiBtn.addEventListener('click', async () => {
            if (confirm("Start a fresh conversation with Swarnav AI Assistant?")) {
                try {
                    await fetch('/api/ai/reset/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'X-CSRFToken': getAiCsrfToken(),
                            'X-Requested-With': 'XMLHttpRequest'
                        }
                    });
                } catch (e) {
                    console.warn("Reset error:", e);
                }

                if (aiChatMessages) {
                    aiChatMessages.innerHTML = `
                        <div class="ai-msg ai-msg-bot">
                            <div class="ai-bubble">
                                🙏 <strong>Jai Shri Krishna / Har Har Mahadev!</strong>
                                <p>Welcome to <strong>Swarnav Tour & Travels</strong>. I am your advanced AI pilgrimage guide, powered by real-time tour itineraries, route elevations, satvik meal plans, and booking records.</p>
                                <p>You can ask me questions in <strong>English, ગુજરાતી, or हिंदी</strong> about our <strong>Char Dham (13 Days)</strong>, <strong>Panch Kedar</strong>, <strong>Jagannath Puri</strong>, <strong>Nepal</strong>, <strong>South India</strong>, or <strong>Kashmir</strong> tours.</p>
                                <p>How may I serve your pilgrimage journey today?</p>
                            </div>
                        </div>
                    `;
                }

                updateSuggestionChips([
                    "What is the 13-day Char Dham Yatra itinerary and price?",
                    "Are these pilgrimages suitable for senior citizens? What about Kedarnath doli or helicopter?",
                    "How much for 4 people on the Char Dham Yatra from Gujarat?",
                    "Tell me about the Nepal Pashupatinath Muktinath tour."
                ]);
            }
        });
    }

    // Initial Chips click binding
    aiChips.forEach(chip => {
        chip.addEventListener('click', () => {
            const prompt = chip.getAttribute('data-prompt');
            if (prompt) processAiQuery(prompt);
        });
    });
});


// --------------------------------------------------------------------------
// 5. Global Form Submission Handler (Secure POST to Django -> WhatsApp)
// --------------------------------------------------------------------------
window.handleInquirySubmit = async function(event) {
    event.preventDefault();
    const form = event.target;
    if (!form) return;

    const isModal = form.id === 'quick-inquiry-form';
    const alertBox = isModal ? document.getElementById('inquiry-alert') : document.getElementById('home-inquiry-alert');
    const submitBtn = isModal ? document.getElementById('modal-submit-btn') : document.getElementById('home-submit-btn');

    // Field selectors based on form
    const tourEl = isModal ? document.getElementById('modal-tour-select') : document.getElementById('home-tour-select');
    const nameEl = isModal ? document.getElementById('modal-user-name') : document.getElementById('home-user-name');
    const phoneEl = isModal ? document.getElementById('modal-user-phone') : document.getElementById('home-user-phone');
    const cityEl = isModal ? document.getElementById('modal-travel-city') : document.getElementById('home-travel-city');
    const countEl = isModal ? document.getElementById('modal-pilgrim-count') : document.getElementById('home-pilgrim-count');
    const notesEl = isModal ? document.getElementById('modal-notes') : document.getElementById('home-notes');
    const consentEl = isModal ? document.getElementById('modal-consent') : document.getElementById('home-consent');

    // Field error containers
    const tourErr = isModal ? document.getElementById('modal-tour-error') : document.getElementById('home-tour-error');
    const nameErr = isModal ? document.getElementById('modal-name-error') : document.getElementById('home-name-error');
    const phoneErr = isModal ? document.getElementById('modal-phone-error') : document.getElementById('home-phone-error');
    const pilgrimsErr = isModal ? document.getElementById('modal-pilgrims-error') : document.getElementById('home-pilgrims-error');
    const consentErr = isModal ? document.getElementById('modal-consent-error') : document.getElementById('home-consent-error');

    // Clear previous errors
    const errorContainers = [tourErr, nameErr, phoneErr, pilgrimsErr, consentErr];
    errorContainers.forEach(el => {
        if (el) {
            el.style.display = 'none';
            el.textContent = '';
        }
    });
    if (alertBox) {
        alertBox.style.display = 'none';
        alertBox.textContent = '';
    }

    const tour = tourEl ? tourEl.value.trim() : '';
    const name = nameEl ? nameEl.value.trim() : '';
    const phone = phoneEl ? phoneEl.value.trim() : '';
    const city = cityEl ? cityEl.value.trim() : '';
    const pilgrims = countEl ? countEl.value.trim() : '';
    const notes = notesEl ? notesEl.value.trim() : '';
    const consentGiven = consentEl ? consentEl.checked : false;
    function getCsrfToken(formEl) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.startsWith('csrftoken=')) {
                    cookieValue = decodeURIComponent(cookie.substring(10));
                    break;
                }
            }
        }
        return cookieValue || formEl?.querySelector('[name=csrfmiddlewaretoken]')?.value || '';
    }

    const csrfToken = getCsrfToken(form);

    // Fast client-side pre-validation
    let hasClientError = false;
    if (!tour) {
        if (tourErr) { tourErr.textContent = 'Please select a tour.'; tourErr.style.display = 'block'; }
        hasClientError = true;
    }
    if (!name) {
        if (nameErr) { nameErr.textContent = 'Your full name is required.'; nameErr.style.display = 'block'; }
        hasClientError = true;
    }
    if (!phone) {
        if (phoneErr) { phoneErr.textContent = 'Phone / WhatsApp number is required.'; phoneErr.style.display = 'block'; }
        hasClientError = true;
    }
    if (!consentGiven) {
        if (consentErr) { consentErr.textContent = 'You must agree to be contacted regarding this inquiry.'; consentErr.style.display = 'block'; }
        hasClientError = true;
    }

    if (hasClientError) {
        if (alertBox) {
            alertBox.style.display = 'block';
            alertBox.style.backgroundColor = '#fef2f2';
            alertBox.style.color = '#991b1b';
            alertBox.style.border = '1px solid #fecaca';
            alertBox.textContent = 'Please complete all required fields and accept the contact agreement.';
        }
        return;
    }

    // UI Loading state & double-click protection
    const originalBtnHtml = submitBtn ? submitBtn.innerHTML : '';
    if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<span>Saving inquiry securely... ⏳</span>';
    }

    try {
        const response = await fetch('/submit-inquiry/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken,
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({
                tour: tour,
                name: name,
                phone: phone,
                departure_city: city,
                total_pilgrims: pilgrims,
                message: notes,
                consent_given: consentGiven,
                csrfmiddlewaretoken: csrfToken
            })
        });

        let data;
        try {
            data = await response.json();
        } catch (parseErr) {
            if (response.status === 403) {
                throw new Error('Your browser security session changed (due to logging in or out). Please refresh the page (F5) and retry.');
            }
            throw new Error('Temporary connection issue. Please refresh and retry.');
        }

        if (response.ok && data.success) {
            if (alertBox) {
                alertBox.style.display = 'block';
                alertBox.style.backgroundColor = '#ecfdf5';
                alertBox.style.color = '#065f46';
                alertBox.style.border = '1px solid #a7f3d0';
                alertBox.innerHTML = `<strong>✓ Inquiry Saved! (Ref: ${data.inquiry_ref})</strong><br>Redirecting to confirmation...`;
            }

            // Close modal if open
            const inquiryModal = document.getElementById('inquiry-modal-overlay');
            if (inquiryModal) {
                inquiryModal.classList.remove('is-active');
                document.body.classList.remove('modal-open');
            }

            // Redirect to success page
            if (data.success_url) {
                window.location.href = data.success_url;
            } else if (data.whatsapp_url) {
                window.location.href = data.whatsapp_url;
            }
        } else {
            // Validation errors returned from Django
            const errorMsg = data.error || 'Please correct the highlighted errors.';
            if (alertBox) {
                alertBox.style.display = 'block';
                alertBox.style.backgroundColor = '#fef2f2';
                alertBox.style.color = '#991b1b';
                alertBox.style.border = '1px solid #fecaca';
                alertBox.innerHTML = `<strong>Inquiry Error:</strong> ${errorMsg}`;
            }

            if (data.errors) {
                if (data.errors.tour && tourErr) { tourErr.textContent = data.errors.tour[0]; tourErr.style.display = 'block'; }
                if (data.errors.name && nameErr) { nameErr.textContent = data.errors.name[0]; nameErr.style.display = 'block'; }
                if (data.errors.phone && phoneErr) { phoneErr.textContent = data.errors.phone[0]; phoneErr.style.display = 'block'; }
                if (data.errors.total_pilgrims && pilgrimsErr) { pilgrimsErr.textContent = data.errors.total_pilgrims[0]; pilgrimsErr.style.display = 'block'; }
                if (data.errors.consent_given && consentErr) { consentErr.textContent = data.errors.consent_given[0]; consentErr.style.display = 'block'; }
            }

            if (submitBtn) {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHtml || '<span>Retry Submission →</span>';
            }
        }
    } catch (err) {
        if (alertBox) {
            alertBox.style.display = 'block';
            alertBox.style.backgroundColor = '#fef2f2';
            alertBox.style.color = '#991b1b';
            alertBox.style.border = '1px solid #fecaca';
            alertBox.innerHTML = `<strong>Inquiry Status:</strong> ${err.message || 'Unable to save inquiry. Please refresh the page and try again.'}`;
        }
        if (submitBtn) {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalBtnHtml || '<span>Retry Submission →</span>';
        }
    }
};



// --------------------------------------------------------------------------
// 6. Language Translation Switcher Controller (English / Hindi / Gujarati)
// --------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    const langLabels = {
        'en': 'English',
        'hi': 'हिन्दी',
        'gu': 'ગુજરાતી'
    };

    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
        return null;
    }

    function getCurrentLang() {
        const saved = localStorage.getItem('swarnav_preferred_lang');
        if (saved && (saved === 'en' || saved === 'hi' || saved === 'gu')) {
            return saved;
        }
        const googtrans = getCookie('googtrans');
        if (googtrans) {
            const lang = googtrans.replace('/en/', '').replace('/auto/', '');
            if (lang === 'hi' || lang === 'gu' || lang === 'en') {
                return lang;
            }
        }
        return 'en';
    }

    function updateLanguageUI(lang) {
        // Update main nav button label
        const mainNavLabel = document.getElementById('main-nav-lang-label');
        if (mainNavLabel) {
            mainNavLabel.textContent = langLabels[lang] || 'Language';
        }

        // Update Dropdown options active state
        const dropdownOptions = document.querySelectorAll('.lang-option-row');
        dropdownOptions.forEach(btn => {
            const btnLang = btn.getAttribute('data-lang');
            if (btnLang === lang) {
                btn.classList.add('is-active');
            } else {
                btn.classList.remove('is-active');
            }
        });

        // Update Top Strip pills active state
        const stripPills = document.querySelectorAll('.strip-lang-pill');
        stripPills.forEach(pill => {
            const pillLang = pill.getAttribute('data-lang');
            if (pillLang === lang) {
                pill.classList.add('is-active');
            } else {
                pill.classList.remove('is-active');
            }
        });
    }

    function switchLanguage(targetLang) {
        localStorage.setItem('swarnav_preferred_lang', targetLang);
        
        // Set cookie for Google Translate
        const cookieVal = '/en/' + targetLang;
        const hostname = window.location.hostname;
        
        document.cookie = `googtrans=${cookieVal}; path=/;`;
        document.cookie = `googtrans=${cookieVal}; path=/; domain=${hostname};`;
        if (hostname !== 'localhost' && !hostname.match(/^\d+\.\d+\.\d+\.\d+$/)) {
            document.cookie = `googtrans=${cookieVal}; path=/; domain=.${hostname};`;
        }

        updateLanguageUI(targetLang);

        // If Google Translate element is in the DOM
        const select = document.querySelector('.goog-te-combo');
        if (select) {
            select.value = targetLang;
            select.dispatchEvent(new Event('change'));
        } else {
            // Reload to let Google translate parse page with new cookie
            window.location.reload();
        }
    }

    // Language dropdown toggle
    const langMenuItem = document.getElementById('lang-menu-item');
    const langDropdownBtn = document.getElementById('lang-dropdown-btn');

    if (langDropdownBtn && langMenuItem) {
        langDropdownBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            langMenuItem.classList.toggle('is-open');
            const isOpen = langMenuItem.classList.contains('is-open');
            langDropdownBtn.setAttribute('aria-expanded', String(isOpen));
        });

        document.addEventListener('click', (e) => {
            if (!langMenuItem.contains(e.target)) {
                langMenuItem.classList.remove('is-open');
                langDropdownBtn.setAttribute('aria-expanded', 'false');
            }
        });
    }

    // Bind click handlers to all language switch buttons
    const allLangButtons = document.querySelectorAll('[data-lang]');
    allLangButtons.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const targetLang = btn.getAttribute('data-lang');
            if (targetLang) {
                switchLanguage(targetLang);
                if (langMenuItem) {
                    langMenuItem.classList.remove('is-open');
                    if (langDropdownBtn) langDropdownBtn.setAttribute('aria-expanded', 'false');
                }
            }
        });
    });

    // Initialize UI on load
    updateLanguageUI(getCurrentLang());
});

