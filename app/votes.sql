SELECT posts.*, count(votes.post_id) as votes FROM posts left join votes on posts.id = votes.post_id group by posts.id;
