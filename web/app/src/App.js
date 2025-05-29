import Header from './components/Header';
import './global.css';

function App() {
  return (
    <div className="App">
      <Header />
      <main>
        <section className="news-section">
          <h2>Latest News</h2>
          <div className="news-articles">
            {/* News articles will go here */}
            <article className="news-article">
              <h3>Sample News Title</h3>
              <p>This is a sample news article summary. More articles will be listed here.</p>
            </article>
          </div>
        </section>
      </main>
    </div>
  );
}

export default App;
