var ap = new APlayer({
    element: document.getElementById('player'),
    narrow: false,
    autoplay: false,
    showlrc: false,
    mutex: true,
    theme: '#ad7a86',
    mode: 'random',
    music: [
        {
            title: '遭英美封杀 卡巴斯基决定关闭美国首都华盛顿办公室',
            author: 'Audiohub',
            url: './audio/a1.mp3',
            pic: './images/logo.jpg'
        },
        {
            title: '未来十年我国清洁能源发电装机量有望超过煤电',
            author: 'Audiohub',
            url: './audio/a2.mp3',
            pic: './images/logo.jpg'
        },
        {
            title: '永辉承认超级物种拟引战投 二马将正面交锋新零售',
            author: 'Audiohub',
            url: './audio/a3.mp3',
            pic: './images/logo.jpg'
        }
    ]
});
