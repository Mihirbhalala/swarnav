/**
 * Swarnav Admin - Tour Departure Date & Month Interactive Handler
 * Enables quick date/month editing from the tour changelist table
 * and reactive conditional display on the tour editing form.
 */

(function () {
    // -------------------------------------------------------------------------
    // 1. Quick-Edit Modal for Changelist Column
    // -------------------------------------------------------------------------
    function createDateModal() {
        if (document.getElementById('sw-date-modal')) return;

        const modalHtml = `
            <div id="sw-date-modal" style="display:none; position:fixed; inset:0; background:rgba(15,23,42,0.6); backdrop-filter:blur(3px); z-index:99999; align-items:center; justify-content:center; padding:16px;">
                <div style="background:#ffffff; border-radius:16px; width:100%; max-width:480px; box-shadow:0 20px 40px rgba(0,0,0,0.25); overflow:hidden; font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif; animation:swPopIn 0.2s ease-out; border:1px solid #e2e8f0;">
                    <!-- Header -->
                    <div style="background:linear-gradient(135deg, #15803d, #047857); padding:18px 22px; color:#ffffff; display:flex; align-items:center; justify-content:space-between;">
                        <div style="display:flex; align-items:center; gap:10px;">
                            <span style="font-size:22px;">📅</span>
                            <div>
                                <h3 style="margin:0; font-size:16px; font-weight:800; color:#ffffff;">Set Tour Date or Month</h3>
                                <div id="sw-modal-tour-name" style="font-size:12px; opacity:0.9; margin-top:2px; font-weight:500;"></div>
                            </div>
                        </div>
                        <button type="button" id="sw-modal-close-btn" style="background:rgba(255,255,255,0.2); border:none; color:#ffffff; font-size:18px; width:30px; height:30px; border-radius:50%; cursor:pointer; display:flex; align-items:center; justify-content:center;">&times;</button>
                    </div>

                    <!-- Body -->
                    <div style="padding:22px;">
                        <p style="margin:0 0 12px 0; font-size:13px; color:#475569; line-height:1.5;">
                            Add the <strong>specific departure date</strong> (e.g. <span style="color:#047857; font-weight:600;">15 Nov 2026</span> or <span style="color:#047857; font-weight:600;">1st Nov – 13th Nov</span>). If exact date is not decided yet, type the <strong>tour start month</strong> (e.g. <span style="color:#047857; font-weight:600;">November 2026</span>).
                        </p>

                        <div style="margin-bottom:14px;">
                            <label for="sw-modal-date-input" style="display:block; font-size:12px; font-weight:800; text-transform:uppercase; letter-spacing:0.04em; color:#1e293b; margin-bottom:6px;">Tour Date / Starting Month</label>
                            <input type="text" id="sw-modal-date-input" placeholder="e.g. 15 Nov 2026 or November 2026"
                                style="width:100%; box-sizing:border-box; padding:10px 14px; border:2px solid #22c55e; border-radius:10px; font-size:14px; font-weight:600; color:#0f172a; outline:none; transition:border-color 0.2s;"
                                onfocus="this.style.borderColor='#15803d'" onblur="this.style.borderColor='#22c55e'">
                        </div>

                        <!-- Quick Month Buttons -->
                        <div style="margin-bottom:18px;">
                            <span style="display:block; font-size:11px; font-weight:700; color:#64748b; margin-bottom:6px; text-transform:uppercase;">Quick Month Select:</span>
                            <div id="sw-quick-months" style="display:flex; flex-wrap:wrap; gap:6px;">
                                <!-- Populated dynamically -->
                            </div>
                        </div>

                        <!-- Action Buttons -->
                        <div style="display:flex; align-items:center; justify-content:flex-end; gap:10px; margin-top:20px; padding-top:14px; border-top:1px solid #f1f5f9;">
                            <button type="button" id="sw-modal-clear-btn" style="padding:9px 16px; border-radius:8px; border:1px solid #cbd5e1; background:#ffffff; color:#64748b; font-size:13px; font-weight:700; cursor:pointer;">Clear Date</button>
                            <button type="button" id="sw-modal-cancel-btn" style="padding:9px 16px; border-radius:8px; border:1px solid #e2e8f0; background:#f8fafc; color:#334155; font-size:13px; font-weight:700; cursor:pointer;">Cancel</button>
                            <button type="button" id="sw-modal-save-btn" style="padding:9px 20px; border-radius:8px; border:none; background:#16a34a; color:#ffffff; font-size:13px; font-weight:800; cursor:pointer; box-shadow:0 2px 6px rgba(22,163,74,0.4);">✓ Save Date</button>
                        </div>
                    </div>
                </div>
            </div>
            <style>
                @keyframes swPopIn {
                    from { opacity: 0; transform: scale(0.95); }
                    to { opacity: 1; transform: scale(1); }
                }
                .sw-quick-pill {
                    background: #f1f5f9;
                    border: 1px solid #e2e8f0;
                    color: #334155;
                    font-size: 11px;
                    font-weight: 700;
                    padding: 4px 10px;
                    border-radius: 9999px;
                    cursor: pointer;
                    transition: all 0.15s ease;
                }
                .sw-quick-pill:hover {
                    background: #dcfce7;
                    border-color: #86efac;
                    color: #15803d;
                    transform: translateY(-1px);
                }
            </style>
        `;

        document.body.insertAdjacentHTML('beforeend', modalHtml);

        // Populate Quick Month Buttons
        const monthsList = [
            'October 2026', 'November 2026', 'December 2026',
            'January 2027', 'February 2027', 'March 2027',
            'April 2027', 'May 2027', 'June 2027'
        ];
        const quickContainer = document.getElementById('sw-quick-months');
        if (quickContainer) {
            monthsList.forEach(m => {
                const btn = document.createElement('button');
                btn.type = 'button';
                btn.className = 'sw-quick-pill';
                btn.innerText = m;
                btn.onclick = () => {
                    const input = document.getElementById('sw-modal-date-input');
                    if (input) input.value = m;
                };
                quickContainer.appendChild(btn);
            });
        }
    }

    let currentSubmitUrl = '';

    window.promptSetTourDate = function (url, tourName, currentDate) {
        createDateModal();
        currentSubmitUrl = url;

        const modal = document.getElementById('sw-date-modal');
        const nameEl = document.getElementById('sw-modal-tour-name');
        const input = document.getElementById('sw-modal-date-input');

        if (nameEl) nameEl.textContent = tourName || 'Tour Package';
        if (input) {
            input.value = currentDate || '';
            setTimeout(() => input.focus(), 100);
        }

        if (modal) modal.style.display = 'flex';

        // Bind events once
        const closeBtn = document.getElementById('sw-modal-close-btn');
        const cancelBtn = document.getElementById('sw-modal-cancel-btn');
        const saveBtn = document.getElementById('sw-modal-save-btn');
        const clearBtn = document.getElementById('sw-modal-clear-btn');

        const closeModal = () => {
            if (modal) modal.style.display = 'none';
        };

        if (closeBtn) closeBtn.onclick = closeModal;
        if (cancelBtn) cancelBtn.onclick = closeModal;

        if (clearBtn) {
            clearBtn.onclick = () => {
                if (input) input.value = '';
                if (currentSubmitUrl) {
                    window.location.href = currentSubmitUrl + '?tour_date=';
                }
            };
        }

        if (saveBtn) {
            saveBtn.onclick = () => {
                const val = (input ? input.value : '').trim();
                if (currentSubmitUrl) {
                    window.location.href = currentSubmitUrl + '?tour_date=' + encodeURIComponent(val);
                }
            };
        }

        // Enter key in input saves
        if (input) {
            input.onkeydown = (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    if (saveBtn) saveBtn.click();
                } else if (e.key === 'Escape') {
                    closeModal();
                }
            };
        }
    };

    // -------------------------------------------------------------------------
    // 2. Change Form: Dynamic Reactive Behavior for Active Tour & Date
    // -------------------------------------------------------------------------
    function initChangeForm() {
        const isActiveCheckbox = document.getElementById('id_is_active');
        const tourDateField = document.getElementById('id_tour_date');
        if (!isActiveCheckbox || !tourDateField) return;

        // Container of the tour_date input
        const tourDateRow = tourDateField.closest('.form-row') || tourDateField.closest('.field-tour_date') || tourDateField.parentElement;
        if (!tourDateRow) return;

        // Create notification banner above the date field
        const helperBanner = document.createElement('div');
        helperBanner.id = 'sw-tour-date-helper-banner';
        helperBanner.style.cssText = 'margin-bottom: 10px; padding: 10px 14px; border-radius: 10px; font-size: 13px; font-weight: 600; display: flex; align-items: center; gap: 8px; transition: all 0.25s ease;';

        // Quick month chips container
        const quickChips = document.createElement('div');
        quickChips.id = 'sw-form-quick-months';
        quickChips.style.cssText = 'display: flex; flex-wrap: wrap; gap: 6px; margin-top: 8px;';
        
        const months = [
            'November 2026', 'December 2026', 'January 2027',
            'April 2027', 'May 2027', 'June 2027', 'October 2027'
        ];
        months.forEach(m => {
            const btn = document.createElement('button');
            btn.type = 'button';
            btn.className = 'sw-quick-pill';
            btn.style.cssText = 'background: #f1f5f9; border: 1px solid #cbd5e1; color: #1e293b; font-size: 11px; font-weight: 700; padding: 4px 10px; border-radius: 9999px; cursor: pointer;';
            btn.innerText = m;
            btn.onclick = () => {
                tourDateField.value = m;
                tourDateField.dispatchEvent(new Event('input', { bubbles: true }));
            };
            quickChips.appendChild(btn);
        });

        tourDateField.parentElement.insertBefore(helperBanner, tourDateField);
        tourDateField.parentElement.appendChild(quickChips);

        function updateState() {
            const isActive = isActiveCheckbox.checked;
            if (isActive) {
                tourDateRow.style.display = '';
                tourDateRow.style.opacity = '1';
                tourDateField.style.borderColor = '#16a34a';
                tourDateField.style.backgroundColor = '#ffffff';
                helperBanner.style.background = '#dcfce7';
                helperBanner.style.border = '1.5px solid #16a34a';
                helperBanner.style.color = '#15803d';
                helperBanner.innerHTML = '<span>✅</span><span><strong>Active Tour:</strong> Enter specific departure date (e.g. 15 Nov 2026) or click a start month below. Highlighted on the live website!</span>';
                quickChips.style.display = 'flex';
            } else {
                tourDateField.style.borderColor = '#cbd5e1';
                tourDateField.style.backgroundColor = '#f8fafc';
                helperBanner.style.background = '#fef2f2';
                helperBanner.style.border = '1.5px solid #f87171';
                helperBanner.style.color = '#b91c1c';
                helperBanner.innerHTML = '<span>⚠️</span><span><strong>Tour is Currently Not Active.</strong> Check <em>"Season / Batch Active"</em> above to activate this tour and show its departure date/month on the website.</span>';
                quickChips.style.display = 'none';
            }
        }

        isActiveCheckbox.addEventListener('change', updateState);
        updateState();
    }

    // Auto-init on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', () => {
            createDateModal();
            initChangeForm();
        });
    } else {
        createDateModal();
        initChangeForm();
    }
})();
