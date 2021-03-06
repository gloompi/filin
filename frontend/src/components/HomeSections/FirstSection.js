import React from 'react'

import VideoBtn from 'components/VideoBtn'

const style = {backgroundImage: `url('/assets/img/main/main.png')`}

export default function FirstSection() {
  return (
    <section className="home__first-section" style={style}>
      <div className="title__wrap">
        <h1 className="main__title">
          Помогаем запустить бизнес на торговой площадке
          <a href="#">
            <img src="/assets/img/main/amazon-black.png" alt="amazon"/>
          </a>
        </h1>
        <VideoBtn />
      </div>
    </section>
  )
}