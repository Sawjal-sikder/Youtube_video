# React Axios
## CRUD in axios
#### 1. Read data to axios

```
import React, { useState } from 'react';
import axios from 'axios';

function DataComponent() {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);

  // URL for API (replace with your actual API URL)
  const apiUrl = 'https://api.example.com/data';

  // Fetch data (READ)
  const fetchData = async () => {
    try {
      const response = await axios.get(apiUrl);
      setData(response.data); // Set fetched data to state
    } catch (error) {
      setError('Failed to fetch data'); // Handle errors
      console.error(error);
    }
  };
```
