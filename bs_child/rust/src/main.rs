use rand::*;

fn main() {
		let mut time = 2023;
    struct Animal {
        id: u32,
        id_0: Option<u32>,
        id_1: Option<u32>,
        birthday: String,
        gen: String,
    }
    let mut animals0 = vec![
        Animal {
            id: 0,
            id_0: None,
            id_1: None,
            birthday: time, // "01/01/2020".to_string(),
            gen: "M".to_string(),
        },
        Animal {
            id: 1,
            id_0: None, // Some(1)
            id_1: None,
            birthday: time, // "02/02/2020".to_string(),
            gen: "F".to_string(),
        },
    ];

	let mut animals1 = vec![
        Animal {
            id: 0,
            id_0: None,
            id_1: None,
            birthday: time, // "01/01/2020".to_string(),
            gen: "M".to_string(),
        },
        Animal {
            id: 1,
            id_0: None, // Some(1)
            id_1: None,
            birthday: time, // "02/02/2020".to_string(),
            gen: "F".to_string(),
        },
    ];

    // let base_count = 100;
    // let count = rand::random::<u32>() % (animals.len() + 100 * base_count) as u32 + 999999;

    for _ in 0..5 {
		time += time + _;
		// random same list
		for _ in 0..animals.len() {
			animals.push(Animal {
				id: animals.len() as u32 + 1, // id - последний + 1
				father_id: // Some(rand::random::<u32>() % animals.len() as u32 + 1), // father_id - случайный id из уже существующих
				mother_id: // Some(rand::random::<u32>() % animals.len() as u32 + 1), // mother_id - то же
				birthday: time,
				gen: "M".to_string(), // gen - M or F (cлучайный)
			});
		}
    }

    // println!("Animals list:"); //выводим результат

    // for animal in &animals {
    // 		println!("{:#?}", animal);
    // }
    println!("Animals list:{}", animals.len()); //выводим результат
}
