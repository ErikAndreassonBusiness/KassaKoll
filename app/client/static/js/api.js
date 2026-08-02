/**
 * api.js - KassaKoll Network Client
 */

// --- ERROR CHECKER ---
const ERROR = {
  handleResponse: async function (response) {
    if (!response.ok) {
      const errorData = await response.json().catch(() => ({}));
      // Fallback to HTTP status if backend didn't provide a detail message
      const errorMessage =
        errorData.detail ||
        `HTTP Error ${response.status}: ${response.statusText}`;
      throw new Error(errorMessage);
    }

    // Handle 204 No Content (e.g. DELETE requests)
    if (response.status === 204) return null;
    return await response.json();
  },
};

// --- MASTER HTTP FUNCTIONS ---

const HTTP_FUNCTIONS = {
  get: async function (endpoint) {
    const response = await fetch(endpoint, {
      method: "GET",
      headers: { Accept: "application/json" },
    });
    return ERROR.handleResponse(response);
  },

  post: async function (endpoint, data) {
    const response = await fetch(endpoint, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    return ERROR.handleResponse(response);
  },

  put: async function (endpoint, data) {
    const response = await fetch(endpoint, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(data),
    });
    return ERROR.handleResponse(response);
  },

  del: async function (endpoint) {
    const response = await fetch(endpoint, {
      method: "DELETE",
    });
    return ERROR.handleResponse(response);
  },
};

// --- DOMAIN HELPER FUNCTIONS ---
// These helpers just supply the route and call the master function

async function loginUser(credentials) {
  return post("/api/auth/login", credentialss);
}
