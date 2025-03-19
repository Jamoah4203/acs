import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client'; // Use React 18 method
import App from './App';
import './index'; // Ensure this file exists

const root = createRoot(document.getElementById('root')!);
root.render(
  <StrictMode>
    <App />
  </StrictMode>
);
