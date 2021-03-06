import React from 'react'

import ParticledElement from 'components/ParticledElement'
import VideoBtn from 'components/VideoBtn'

export default function FifthSection() {
  return (
    <section className="home__fifth-section">
      <ParticledElement height="100%" />
      <div className="container home__fifth-container">
        <div className="macbook__pic">
          <img src="/assets/img/main/macbook.png" alt="macbook"/>
          <VideoBtn classToAdd="banner__get-link" />
        </div>
        <h2 className="home__fifth-title bold">
          Посмотрите видео о том, как найти 
          <span className="orange"> товар для успешного </span>
           старта на <img src="/assets/img/main/arrow.png" alt="amazon"/>
        </h2>
      </div>
    </section>
  )
}