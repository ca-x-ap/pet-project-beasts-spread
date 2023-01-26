fn main() {
    struct Animal {
      id: u32,
      father_id: Option<u32>,
      mather_id: Option<u32>,
      birthday: String,
  }

  impl Animal {
      fn spread(&self) {
          // logic to spread animals on rust goes here 
      } 
  }

  let mut count = 0u32;

  println!("Let's count until infinity!");

  // Infinite loop
  loop {
      count += 1;

      if count == 3 {
          println!("three");

          // Skip the rest of this iteration
          continue;
      }

      println!("{}", count);

      if count == 5 {
          println!("OK, that's enough");

          // Exit this loop
          break;
      }
  }
}
