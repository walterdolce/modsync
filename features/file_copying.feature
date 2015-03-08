Feature: File copying
  In order to keep files in sync with the destination directory I specify
  As a developer
  I want my files to be copied across the various destinations

  Scenario: Newly created files get copied in the various destinations
    Given there is a directory
      | directory    |
      | framework_v1 |
      | framework_v2 |
      | source_dir   |
    And I specify "source_dir" as the source directory
    And I specify the target directories
     | target_dir   |
     | framework_v1 |
     | framework_v2 |
    And I run modsync
    And I create a file "my_file.txt" in "source_dir" directory
    Then file "my_file.txt" should be copied in
     | target_dir   |
     | framework_v1 |
     | framework_v2 |