/**
 * login.js - Handles UI interactions for the Fortnox OAuth login page
 */

// DOM DICTIONARY
const DOM = {
  // We only need the connect button and error message container
  connectBtn: document.getElementById("fortnox-connect-btn"),
  errorMessage: document.getElementById("error-message"),
};

// STATE
const state = {
  isLoading: false,
};

// UI DICTIONARY
const UI = {
  showError(message) {
    if (!DOM.errorMessage) return;
    DOM.errorMessage.textContent = message;
    DOM.errorMessage.classList.remove("d-none");
  },

  clearError() {
    if (!DOM.errorMessage) return;
    DOM.errorMessage.textContent = "";
    DOM.errorMessage.classList.add("d-none");
  },

  setLoading(loading) {
    state.isLoading = loading;
    if (!DOM.connectBtn) return;

    // Bootstrap handles disabled states on buttons and pointer-events on anchor tags
    if (loading) {
      DOM.connectBtn.classList.add("disabled");
      DOM.connectBtn.innerHTML =
        '<span class="spinner-border spinner-border-sm" role="status"></span> Omdirigerar till Fortnox...';
    } else {
      DOM.connectBtn.classList.remove("disabled");
      DOM.connectBtn.innerHTML = "Koppla till Fortnox";
    }
  },
};

// EVENT HANDLERS
function handleConnectClick(event) {
  // Guard against double clicks
  if (state.isLoading) {
    event.preventDefault();
    return;
  }

  UI.clearError();
  UI.setLoading(true);
}

// INITIALIZATION
function initLogin() {
  if (!DOM.connectBtn) return;
  DOM.connectBtn.addEventListener("click", handleConnectClick);
}

// Run initialization once HTML parsing is complete
document.addEventListener("DOMContentLoaded", initLogin);
