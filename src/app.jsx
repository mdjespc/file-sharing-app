import React, { useState, useEffect } from "react";
import axios from "axios";

const NetworkInfo = () => {
  const [ipAddress, setIpAddress] = useState("Fetching...");
  const [devices, setDevices] = useState([]);

  useEffect(() => {
    const getLocalIP = async () => {
      try {
        const pc = new RTCPeerConnection({ iceServers: [] });
        pc.createDataChannel("");
        pc.onicecandidate = (event) => {
          if (event.candidate) {
            const ipRegex = /(\d+\.\d+\.\d+\.\d+)/;
            const match = ipRegex.exec(event.candidate.candidate);
            if (match) {
              setIpAddress(match[1]);
              registerDevice(match[1]);
              pc.close();
            }
          }
        };
        await pc.createOffer().then((offer) => pc.setLocalDescription(offer));
      } catch (error) {
        setIpAddress("Could not retrieve IP");
      }
    };

    const registerDevice = async (ip) => {
      await axios.post("http://localhost:5000/register", { ip });
      fetchDevices();
    };

    const fetchDevices = async () => {
      const response = await axios.get("http://localhost:5000/devices");
      setDevices(response.data.devices);
    };

    getLocalIP();
    const interval = setInterval(fetchDevices, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h2>Network Information</h2>
      <p><strong>Your Local IP Address:</strong> {ipAddress}</p>
      <h3>Connected Devices:</h3>
      <ul>
        {devices.map((device, index) => (
          <li key={index}>{device}</li>
        ))}
      </ul>
    </div>
  );
};

export default NetworkInfo;
