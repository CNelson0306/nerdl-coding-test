import Header from './components/Header';
import './global.css';

// Imported the newly created news component
import News from './components/News';


function App() {
  return (
    <div className="App">
      <Header />
      <main>
        
        <News />

      </main>
    </div>
  );
}

export default App;
