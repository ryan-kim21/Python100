import React from "react";
import Slider from "react-slick";

class ImageSlider extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      images: [],
    };
  }

  componentDidMount() {
    // API를 호출하여 이미지 파일 정보를 받아옴
    fetch("http://example.com/images")
      .then((response) => response.json())
      .then((data) => {
        // 받아온 데이터를 images state에 저장
        this.setState({ images: data });
      })
      .catch((error) => console.error(error));
  }

  render() {
    const settings = {
      dots: true,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1,
    };

    const { images } = this.state;

    return (
      <Slider {...settings}>
        {images.map((image) => (
          <div key={image.id}>
            <img src={image.src} alt={image.alt} />
          </div>
        ))}
      </Slider>
    );
  }
}

export default ImageSlider;