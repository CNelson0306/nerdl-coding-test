import React from 'react'
import { useEffect, useState } from 'react';


// I used free images from the internet and imported them here
// to be used in the News component.
import img1 from '../assets/img1.jpg';
import img2 from '../assets/img2.jpg';
import img3 from '../assets/img3.jpg';
import img4 from '../assets/img4.jpg';


function News() {

    {/*Fetch the data from the database */}

    const [articles, setArticles] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch('http://api.nerdl.test/public/articles')
        .then((response) => response.json())
        .then((data) => {
            setArticles(data.articles);
            setLoading(false);
        })
        .catch((error) => {
            console.error('Error fetching articles:', error);
            setLoading(false);
        });
    }, []);

    if (loading) return <div>Fetching Data...</div>;

    {/* I used the main news article like this and used slice().map for the others */} 

    const latestArticle = articles[0];

    return (
        <>
        <h2 className='news-heading'>News</h2>
            <section className="news-section">
            <div className="news-articles">
                {/* News articles will go here */}          
            
            <div className='latest-news'>
                <h3>Latest News</h3>
                <div className='latest-news-container'>
                <article className="latest-news-article">
                    <img src={img1} alt='Falcon Image' />
                <div className='news-content'>
                    <h3>{latestArticle.title}</h3>
                        <p>
                            <span>&#129413; </span> 
                             {latestArticle.excerpt}
                        </p>
                    <div className='read-more'>
                        <h3>Just Now</h3>
                        <button className='read-more-btn'>read more</button>
                    </div>
                        <h4>{latestArticle.author}</h4>
                    </div>
                </article>
                </div>
            </div>
            </div>

            <div className='trending-news'>
            <h3>Trending</h3>

            {articles.slice(1,2).map(article => (
            <article className='trending-article'>
                <div className='trending-content'>
                    <h3>{article.title}</h3>
                        <p>
                            <span>&#128522; </span> 
                             {article.excerpt}
                        </p>
                    <h4>{article.author}</h4>
                </div>
                <img src={img2} alt='React Image' />
            </article>
            ))}

            {articles.slice(2,3).map(article => (
            <article className='trending-article'>
                <div className='trending-content'>
                    <h3>{article.title}</h3>
                        <p>
                            <span>&#128187; </span> 
                             {article.excerpt}
                        </p>
                    <h4>{article.author}</h4>
                </div>
                <img src={img3} alt='Tech Company Image' />
            </article>
            ))}

            {articles.slice(3,4).map(article => (
            <article className='trending-article'>
                <div className='trending-content'>
                <h3>{article.title}</h3>
                    <p>
                        <span>&#129689; </span> 
                         {article.excerpt}
                    </p>
                    <h4>{article.author}</h4>
                </div>
                <img src={img4} alt='Crypto Image' />
            </article> 
            ))}

            </div>
            </section>
        </>
  )
}


export default News
