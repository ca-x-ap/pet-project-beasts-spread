use rand::*;

fn spread_beasts(min_live_time: i32, live_time: i32, start_count: i32, years: i32, min_children_count: i32, children_count: i32) -> Vec<Vec<Vec<HashMap<&str, String>>>> {
	let mut time = 2023;
	let mut beasts = vec![vec![vec![], vec![]], vec![vec![], vec![]]];

	// fn randomword(length: usize) -> String {
	// 	let letters = "abcdefghijklmnopqrstuvwxyz";
	// 	(0..length).map(|_| {
	// 		let idx = rand::thread_rng().gen_range(0, letters.len());
	// 		letters.chars().nth(idx).unwrap()
	// 	}).collect()
	// }

	for _ in 0..start_count/2 {
		beasts[0][0].push(hashmap!{
			"id" => beasts[0][0].len().to_string(),
			"id_0" => None.to_string(),
			"id_1" => None.to_string(),
			"birthday" => time.to_string(),
			// "gen" => format!("{} {}", randomword(6), randomword(6)) });
		})
		beasts[0][1].push(hashmap!{
			"id" => beasts[0][1].len().to_string(),
			"id_0" => None.to_string(),
			"id_1" => None.to_string(),
			"birthday" => time.to_string(),
			// "gen" => format!("{} {}", randomword(6), randomword(6)) });
		})
	}

	for count in 0..years {
		time += count;
		beasts[0][0].shuffle();

		for (beast0, beast1) in beasts[0][0].iter().zip(beasts[0][1].iter()) {
			let current_children_count = rand::thread_rng().gen_range(min_children_count, children_count);
			for _ in 0..current_children_count {
				let list_number = rand::thread_rng().gen_range(0, 1);
				beasts[0][list_number].push({
					id: beasts[0][list_number].len(),
					id_0: beast0.id,
					id_1: beast1.id,
					birthday: time,
					// gen: format!("{} {}", beast0.gen.split(" ")[0], beast1.gen.split(" ")[1])
				});

				if beast0.birthday + rand::thread_rng().gen_range(min_live_time, live_time) < time {
					beasts[1][0].push(beast0);
					beasts[0][0].remove(beast0);
				}
				if beast1.birthday + rand::thread_rng().gen_range(min_live_time, live_time) < time {
					beasts[1][1].push(beast1);
					beasts[0][1].remove(beast0);
				}
			}
		}
	}
}

fn main() {

}
