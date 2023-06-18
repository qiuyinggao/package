def simulate_package_loading():
    max_items = int(input("Enter the maximum number of items to be shipped: "))
    packages_sent = 0
    total_weight_sent = 0
    max_unused_capacity = 0
    max_unused_capacity_package = 0

    current_package_weight = 0

    for i in range(1, max_items + 1):
        item_weight = float(input("Enter the weight of item {}: ".format(i)))

        if item_weight == 0:
            # Terminate the program if an item with weight 0 is given
            break

        if item_weight < 1 or item_weight > 10:
            print("Invalid item weight. Item weight must be between 1 and 10 kg.")
            continue

        if current_package_weight + item_weight > 20:
            # Send the current package and start a new one
            packages_sent += 1
            total_weight_sent += current_package_weight
            unused_capacity = 20 - current_package_weight
            if unused_capacity > max_unused_capacity:
                max_unused_capacity = unused_capacity
                max_unused_capacity_package = packages_sent

            current_package_weight = item_weight
        else:
            # Add the item to the current package
            current_package_weight += item_weight

    # Check if there's an unfinished package
    if current_package_weight > 0:
        packages_sent += 1
        total_weight_sent += current_package_weight
        unused_capacity = 20 - current_package_weight
        if unused_capacity > max_unused_capacity:
            max_unused_capacity = unused_capacity
            max_unused_capacity_package = packages_sent

    print("Number of packages sent: {}".format(packages_sent))
    print("Total weight of packages sent: {} kg".format(total_weight_sent))
    print("Total 'unused' capacity: {} kg".format(packages_sent * 20 - total_weight_sent))
    print("Package with the most 'unused' capacity: Package {}, Unused Capacity: {} kg".format(
        max_unused_capacity_package, max_unused_capacity))


simulate_package_loading()

