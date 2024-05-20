const API = import.meta.env.VITE_API_HOST;

export const getCollections = async (username, token) => {
  const collectionsUrl = API + `/${username}/collections`;
  const fetchConfig = {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(collectionsUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    return data.collections;
  }
};

export const getCollection = async (username, collection_id, token) => {
  const collectionUrl = API + `/${username}/collections/${collection_id}`;
  const fetchConfig = {
    method: "get",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(collectionUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    return data;
  }
};

export const createCollection = async (username, collectionData, token) => {
  const collectionsUrl = API + `/${username}/collections`;
  const body = JSON.stringify(collectionData);
  const fetchConfig = {
    method: "post",
    body: body,
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(collectionsUrl, fetchConfig);
  if (response.ok) {
    const data = await response.json();
    return { status: true, collection_id: data.id };
  } else {
    return { status: false };
  }
};

export const updateCollection = async (
  username,
  collection_id,
  collectionData,
  token
) => {
  const collectionsUrl = API + `/${username}/collections/${collection_id}`;
  const body = JSON.stringify(collectionData);
  const fetchConfig = {
    method: "put",
    body: body,
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(collectionsUrl, fetchConfig);
  if (response.ok) {
    return true;
  } else {
    return false;
  }
};

export const deleteCollection = async (username, collection_id, token) => {
  const collectionUrl = API + `/${username}/collections/${collection_id}`;
  const fetchConfig = {
    method: "delete",
    headers: {
      "Content-Type": "application/json",
      Authorization: "Bearer " + token,
    },
  };
  const response = await fetch(collectionUrl, fetchConfig);
  if (response.ok) {
    return { result: true };
  } else {
    const data = await response.json();
    return { result: false, error: data.detail };
  }
};

export const getCollectionItemCount = async (
  username,
  collection_id,
  token
) => {
  const itemsUrl =
    API + `/${username}/collections/${collection_id}/items/count`;
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
    return data.count;
  }
};
