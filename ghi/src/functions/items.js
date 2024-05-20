const API = import.meta.env.VITE_API_HOST;

export const getItems = async (username, collection_id, token) => {
  const itemsUrl = API + `/${username}/collections/${collection_id}/items`;
  const fetchConfig = {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(itemsUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    return data.items;
  }
};

export const getItem = async (username, collection_id, item_id, token) => {
  const itemUrl =
    API + `/${username}/collections/${collection_id}/items/${item_id}`;
  const fetchConfig = {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(itemUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    return data;
  }
};

export const createItem = async (username, collection_id, itemData, token) => {
  const itemsUrl = API + `/${username}/collections/${collection_id}/items`;
  const body = JSON.stringify(itemData);
  const fetchConfig = {
    method: "post",
    body: body,
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(itemsUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    return { status: true, item_id: data.id };
  } else {
    return { status: false };
  }
};

export const updateItem = async (
  username,
  collection_id,
  item_id,
  itemData,
  token
) => {
  const itemUrl =
    API + `/${username}/collections/${collection_id}/items/${item_id}`;
  const body = JSON.stringify(itemData);
  const fetchConfig = {
    method: "put",
    body: body,
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(itemUrl, fetchConfig);
  if (response.ok) {
    return true;
  } else {
    return false;
  }
};

export const deleteItem = async (username, collection_id, item_id, token) => {
  const itemUrl =
    API + `/${username}/collections/${collection_id}/items/${item_id}`;
  const fetchConfig = {
    method: "delete",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(itemUrl, fetchConfig);
  if (response.ok) {
    return { result: true };
  } else {
    const data = await response.json();
    return { result: false, error: data.detail };
  }
};
