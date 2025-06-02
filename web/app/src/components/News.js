import React from 'react'
import { useEffect, useState } from 'react';

import img1 from '../assets/img1.png';
import img2 from '../assets/img2.png';
import img3 from '../assets/img3.png';


function News() {

  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetch('http://api.nerdl.test/public/articles')
      .then((response) => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then((data) => {
        setArticles(data);
        setLoading(false);
      })
      .catch((err) => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading articles...</p>;
  if (error) return <p>Error: {error}</p>;


  return (
    <>
    <h2 className='news-heading'>News</h2>
        <section className="news-section">
          <div className="news-articles">
            {/* News articles will go here */}          
          
          <div className='latest-news'>
              <h3>Latest News</h3>

            <div className='latest-news-container'>

            {articles.slice(0,1).map((article) => (

              <article className="latest-news-article">
                
                <img src={img1} alt='Bitcoin image' />
                <div className='news-content'>

                <h3>{article.category}</h3>

                {/*<h3>Bitcoin</h3>*/}
                
                {/*<p><span>&#127919;</span> Feeling Lucky: James Wynn's $1bn Bitcoin Bet Ends in a $60m Flameout</p>*/}
                
                <p>{article.excerpt}</p>
              
              <div className='read-more'>
                <h3>Just Now</h3>
                <button className='read-more-btn'>read more</button>
              </div>
              <h4>G.Lomas</h4>
                </div>
              </article>
            ))}
              </div>
          </div>
          </div>

          

          <div className='trending-news'>
           <h3>Trending</h3>

          <article className='trending-article'>
            <div className='trending-content'>
              <h3>Bitcoin</h3>
                <p><span>&#127919;</span> Feeling Lucky: James Wynn's $1bn Bitcoin Bet Ends in a $60m Flameout</p>
              <h4>G.Lomas</h4>
            </div>
            <img src={img1} alt='Bitcoin Image' />
          </article>

          <article className='trending-article'>
            <div className='trending-content'>
              <h3>Finance</h3>
                <p><span>&#129534;</span> Hyperliquid Makes Its Case for 24/7 Cryto Derivatives Trading to US</p>
              <h4>G.Lomas</h4>
            </div>
            <img src={img2} alt='Crypto Image' />
          </article>

          <article className='trending-article'>
            <div className='trending-content'>
              <h3>Cryptocurrency</h3>
                <p><span>&#128747;</span> Crypto Travellers Spend Big - And Often</p>
              <h4>L.Abate</h4>
            </div>
            <img src={img3} alt='Crypto Travellers Image' />
          </article>
          
            
        </div>
        </section>
    </>
  )
}


export default News
