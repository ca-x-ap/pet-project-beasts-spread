use rand::*;

// fn main() {
//     let mut animals = vec![
//         Animal {
//             id: 1,
//             father_id: None,
//             mother_id: None,
//             birthday: "01/01/2020",
//             gen: "M",
//         },
//         Animal {
//             id: 2,
//             father_id: Some(1),
//             mother_id: None,
//             birthday: "02/02/2020",
//             gen: "F",
//         },
//     ];

//     for _ in 0..34 {
//         // итерируем 34 раза для добавления 34 животных в наш список

//         let new_animal = Animal {
//             // создаем новое животное со случайными полями (кроме id)
//             id: animals.len() as u32 + 1, // id - последний + 1

//             father_id: Some(rand::random::<u32>() % animals.len() as u32 + 1), // father_id - случайный id из уже существующих

//             mother_id: Some(rand::random::<u32>() % animals.len() as u32 + 1), // mother_id - то же

//             birthday: format!(
//                 "{}/{}/{}",
//                 rand::random::<u8>(),
//                 rand::random::<u8>(),
//                 rand::random::<u16>()
//             ), // birthday - cлучайный

//             gen: if rand::random() { "M" } else { "F" }, // gen - M or F (cлучайный)
//         };

//         animals.push(new_animal); //добавляем новое животное в список
//     }

//     println!("Animals list:"); //выводим результат

//     for animal in &animals {
//         println!("{:#?}", animal);
//     }
// }

fn main() {
	struct Animal {
			id: u32,
			father_id: Option<u32>,
			mother_id: Option<u32>,
			birthday: String,
			gen: String
	}
	let mut animals = vec![
			Animal {
					id: 1,
					father_id: None,
					mother_id: None,
					birthday: "01/01/2020".to_string(),
					gen: "M".to_string(),
			},
			Animal {
					id: 2,
					father_id: Some(1),
					mother_id: None,
					birthday: "02/02/2020".to_string(),
					gen: "F".to_string(),
			},
	];

	let base_count = 2;

	let count = rand::random::<u32>() % (animals.len() + 100 * base_count) as u32 + 999999;

	for _ in 0..count {
			// итерируем 34 раза для добавления 34 животных в наш список

			let new_animal = Animal { // создаем новое животное со случайными полями (кроме id)
					id: animals.len() as u32 + 1, // id - последний + 1
					father_id: Some(rand::random::<u32>() % animals.len() as u32 + 1), // father_id - случайный id из уже существующих
					mother_id: Some(rand::random::<u32>() % animals.len() as u32 + 1), // mother_id - то же
					birthday: format!("{}/{}/{}",
							1,
							2,
							3
					), // birthday - cлучайный

					gen: "M".to_string(), // gen - M or F (cлучайный)
			};

			animals.push(new_animal); //добавляем новое животное в список
	}

	// println!("Animals list:"); //выводим результат

	// for animal in &animals {
	// 		println!("{:#?}", animal);
	// }
		println!("Animals list:{}", animals.len()); //выводим результат

}
