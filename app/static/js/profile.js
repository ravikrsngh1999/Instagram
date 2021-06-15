//Making the modal work
let imgPosts = document.querySelectorAll('.img-wrapper>img');
let postModal = document.querySelector('.modal');
let closeModalBtn = document.querySelector('.close-modal-btn');

imgPosts.forEach(function (imgPost) {
	imgPost.addEventListener('click', showPost);
});

postModal.addEventListener('click', function (event) {
	if (event.target == postModal) {
		hidePost();
	}
});

closeModalBtn.addEventListener('click', hidePost);
document.addEventListener('keydown', function (e) {
	if (e.key === 'Escape') hidePost();
});

function showPost(e) {
	postModal.style.display = 'flex';
	var postid = e.target.getAttribute('data-catid')
	$.ajax({
		type:"GET",
		url:"/getpostdetails/",
		data: {
			postid:postid,
		},
		success: function(data){
			document.getElementById('modal-post-content').src= "/media/" + data[0]
			document.getElementById('modal-username').innerText = data[1]
			document.getElementById('modal-caption').innerHTML = "<a href=\"\">"+data[1]+"</a>" + data[2]
		}
	})
	document.body.style.overflowY = 'hidden';
}

function hidePost(event) {
	postModal.style.display = 'none';
	document.body.style.overflowY = 'auto';
}

// Switching active nav tabs
let navTabs = document.querySelectorAll('.nav-tab');
let activeNavTab = document.querySelector('.active-nav-tab');

navTabs.forEach(function (tab) {
	tab.addEventListener('click', switchTab);
});

function switchTab(event) {
	let tab = event.target;

	activeNavTab.classList.remove('active-nav-tab');
	tab.classList.add('active-nav-tab');

	activeNavTab = tab;
}
