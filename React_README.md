# React Axios
### CRUD in axios
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
#### 2. Create data to axios

```
  // Create data (CREATE)
  const createData = async (newData) => {
    try {
      const response = await axios.post(apiUrl, newData);
      setData([...data, response.data]); // Add new data to state
    } catch (error) {
      setError('Failed to create data'); // Handle errors
      console.error(error);
    }
  };
```
#### 3. Update data to axios

```
 // Update data (UPDATE)
  const updateData = async (id, updatedData) => {
    try {
      const response = await axios.put(`${apiUrl}/${id}`, updatedData);
      const updatedDataList = data.map((item) =>
        item.id === id ? response.data : item
      );
      setData(updatedDataList); // Update state with the modified data
    } catch (error) {
      setError('Failed to update data'); // Handle errors
      console.error(error);
    }
  };
```
#### 4. Delete data to axios

```
// Delete data (DELETE)
  const deleteData = async (id) => {
    try {
      await axios.delete(`${apiUrl}/${id}`);
      const updatedDataList = data.filter((item) => item.id !== id);
      setData(updatedDataList); // Remove deleted data from state
    } catch (error) {
      setError('Failed to delete data'); // Handle errors
      console.error(error);
    }
  };

```
